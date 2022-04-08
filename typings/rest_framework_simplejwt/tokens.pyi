"""
This type stub file was generated by pyright.
"""

from django.conf import settings

class Token:
    """
    A class which validates and"""
    token_type = ...
    lifetime = ...
    def __init__(self, token=..., verify=...) -> None:
        """
        !!!! IMPORTANT !!!! MUS"""
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __getitem__(self, key): # -> Any:
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def __delitem__(self, key): # -> None:
        ...
    
    def __contains__(self, key): # -> bool:
        ...
    
    def get(self, key, default=...): # -> Any | None:
        ...
    
    def __str__(self) -> str:
        """
        Signs and returns a tok"""
        ...
    
    def verify(self): # -> None:
        """
        Performs additional val"""
        ...
    
    def verify_token_type(self): # -> None:
        """
        Ensures that the token """
        ...
    
    def set_jti(self): # -> None:
        """
        Populates the configure"""
        ...
    
    def set_exp(self, claim=..., from_time=..., lifetime=...): # -> None:
        """
        Updates the expiration """
        ...
    
    def set_iat(self, claim=..., at_time=...): # -> None:
        """
        Updates the time at whi"""
        ...
    
    def check_exp(self, claim=..., current_time=...): # -> None:
        """
        Checks whether a timest"""
        ...
    
    @classmethod
    def for_user(cls, user): # -> Self@Token:
        """
        Returns an authorizatio"""
        ...
    
    _token_backend = ...
    @property
    def token_backend(self): # -> Any:
        ...
    
    def get_token_backend(self): # -> Any:
        ...
    


class BlacklistMixin:
    """
    If the `rest_framework_simp"""
    if "rest_framework_simplejwt.token_b" in settings.INSTALLED_APPS:
        def verify(self, *args, **kwargs): # -> None:
            ...
        
        def check_blacklist(self): # -> None:
            """
            Checks if this toke"""
            ...
        
        def blacklist(self): # -> Tuple[Any, bool]:
            """
            Ensures this token """
            ...
        
        @classmethod
        def for_user(cls, user):
            """
            Adds this token to """
            ...
        


class SlidingToken(BlacklistMixin, Token):
    token_type = ...
    lifetime = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class AccessToken(Token):
    token_type = ...
    lifetime = ...


class RefreshToken(BlacklistMixin, Token):
    token_type = ...
    lifetime = ...
    no_copy_claims = ...
    access_token_class = AccessToken
    @property
    def access_token(self): # -> access_token_class:
        """
        Returns an access token"""
        ...
    


class UntypedToken(Token):
    token_type = ...
    lifetime = ...
    def verify_token_type(self): # -> None:
        """
        Untyped tokens do not v"""
        ...
    


