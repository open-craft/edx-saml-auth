from third_party_auth.provider import BaseProvider
from . import backend

class PingOneBackend(backend.SAMLBaseAuth):
    name = 'ping-one'

    def get_user_details(self, response):
        details = super(PingOneBackend, self).get_user_details(response)
        details['username'] = details.get('fullname', '').replace(' ', '')
        return details


class PingOneProvider(BaseProvider):
    BACKEND_CLASS = PingOneBackend
    ICON_CLASS = 'icon-signin'
    NAME = 'PingOne'

    SETTINGS = {
        'SOCIAL_AUTH_PING_ONE_ASSERTION_CONSUMER_SERVICE_URL': None,
        'SOCIAL_AUTH_PING_ONE_ISSUER': None,
        'SOCIAL_AUTH_PING_ONE_NAME_IDENTIFIER_FORMAT': None,
        'SOCIAL_AUTH_PING_ONE_IDP_SSO_TARGET_URL': None,
        'SOCIAL_AUTH_PING_ONE_IDP_CERT_FINGERPRINT': None,
        'SOCIAL_AUTH_PING_ONE_EXTRA_ATTRIBUTES': None,
    }

    @classmethod
    def get_email(cls, provider_details):
        return provider_details('email')

    @classmethod
    def get_name(cls, provider_details):
        return provider_details('fullname')
