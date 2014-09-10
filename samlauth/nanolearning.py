from third_party_auth.provider import BaseProvider

from . import pingone

class NanolearningProvider(BaseProvider):
    BACKEND_CLASS = pingone.PingOneBackend
    ICON_CLASS = 'icon-signin'
    NAME = 'Applied Materials/Eteris account'

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
        return provider_details.get('email')

    @classmethod
    def get_name(cls, provider_details):
        return provider_details.get('fullname')
