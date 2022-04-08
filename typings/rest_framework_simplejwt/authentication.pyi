"""
This type stub file was generated by pyright.
"""

from rest_framework import authentication
from .settings import api_settings

AUTH_HEADER_TYPES = ...
if notisinstance(api_settings.AUTH_HEADER_TYPES, (list, tuple)):
    AUTH_HEADER_TYPES = ...
AUTH_HEADER_TYPE_BYTES = ...

class JWTAuthentication(authentication.BaseAuthentication):
    """
    An authentication plugin th"""

    www_authenticate_realm = ...
    media_type = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def authenticate(self, request): ...
    def authenticate_header(self, request): ...
    def get_header(self, request):  # -> bytes:
        """
        Extracts the header con"""
        ...
    def get_raw_token(self, header):  # -> None:
        """
        Extracts an unvalidated"""
        ...
    def get_validated_token(self, raw_token):
        """
        Validates an encoded JS"""
        ...
    def get_user(self, validated_token):  # -> Any:
        """
        Attempts to find and re"""
        ...

class JWTTokenUserAuthentication(JWTAuthentication):
    def get_user(self, validated_token):  # -> Any:
        """
        Returns a stateless use"""
        ...

def default_user_authentication_rule(user): ...
