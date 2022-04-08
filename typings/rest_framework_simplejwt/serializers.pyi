"""
This type stub file was generated by pyright.
"""

from rest_framework import serializers
from .settings import api_settings
from .tokens import RefreshToken, SlidingToken

if api_settings.BLACKLIST_AFTER_ROTATION:
    ...
class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class TokenObtainSerializer(serializers.Serializer):
    username_field = ...
    token_class = ...
    default_error_messages = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def validate(self, attrs): # -> dict[Unknown, Unknown]:
        ...
    
    @classmethod
    def get_token(cls, user):
        ...
    


class TokenObtainPairSerializer(TokenObtainSerializer):
    token_class = RefreshToken
    def validate(self, attrs): # -> dict[Unknown, Unknown]:
        ...
    


class TokenObtainSlidingSerializer(TokenObtainSerializer):
    token_class = SlidingToken
    def validate(self, attrs): # -> dict[Unknown, Unknown]:
        ...
    


class TokenRefreshSerializer(serializers.Serializer):
    refresh = ...
    access = ...
    token_class = RefreshToken
    def validate(self, attrs): # -> dict[str, str]:
        ...
    


class TokenRefreshSlidingSerializer(serializers.Serializer):
    token = ...
    token_class = SlidingToken
    def validate(self, attrs): # -> dict[str, str]:
        ...
    


class TokenVerifySerializer(serializers.Serializer):
    token = ...
    def validate(self, attrs): # -> dict[Unknown, Unknown]:
        ...
    


class TokenBlacklistSerializer(serializers.Serializer):
    refresh = ...
    token_class = RefreshToken
    def validate(self, attrs): # -> dict[Unknown, Unknown]:
        ...
    


