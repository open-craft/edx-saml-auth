from urlparse import urlparse
from onelogin import saml
from social.backends.base import BaseAuth


class SAMLVerificationFailure(Exception):
    pass


class SAMLBaseAuth(BaseAuth):
    saml_response = None

    def auth_url(self):
        url = saml.AuthRequest.create(
            assertion_consumer_service_url=self.setting('ASSERTION_CONSUMER_SERVICE_URL'),
            issuer=self.setting('ISSUER'),
            name_identifier_format=self.setting('NAME_IDENTIFIER_FORMAT'),
            idp_sso_target_url=self.setting('IDP_SSO_TARGET_URL')
        )
        return url

    def get_user_details(self, response):
        details = {'name_id': self.saml_response.name_id}

        attributes = self.setting('EXTRA_ATTRIBUTES')
        for name, attr in attributes:
            details[name] = (self.saml_response.get_assertion_attribute_value(attr) or [None])[0]

        return details

    def get_user_id(self, details, response):
        return details['name_id']

    def auth_complete(self, *args, **kwargs):
        uri = urlparse(self.strategy.build_absolute_uri())
        request_info = {
            'server_name': uri.hostname,
            'path_info': uri.path,
            'https': 'on' if uri.scheme == 'https' else 'off',
            'script_name': '',
        }
        if uri.port:
            request_info['server_port'] = uri.port

        response = self.strategy.request_data()

        self.saml_response = saml.Response(
            request_info,
            response.get('SAMLResponse'),
            self.setting('IDP_CERT_FINGERPRINT'),
            issuer=self.setting('ISSUER')
        )

        if not self.saml_response.is_valid():
            raise SAMLVerificationFailure('SAML response signature invalid')

        kwargs.update({
            'response': response,
            'backend': self,
        })

        return self.strategy.authenticate(*args, **kwargs)
