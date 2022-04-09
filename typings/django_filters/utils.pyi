"""
This type stub file was generated by pyright.
"""

def deprecate(msg, level_modifier=...): # -> None:
    ...

class MigrationNotice(DeprecationWarning):
    url = ...
    def __init__(self, message) -> None:
        ...
    


class RenameAttributesBase(type):
    """
    Handles the deprecation pat"""
    renamed_attributes = ...
    def __new__(metacls, name, bases, attrs): # -> Self@RenameAttributesBase:
        ...
    
    def get_name(metacls, name):
        """
        Get the real attribute """
        ...
    
    def __getattr__(metacls, name): # -> Any:
        ...
    
    def __setattr__(metacls, name, value): # -> None:
        ...
    


def try_dbfield(fn, field_class): # -> None:
    """
    Try ``fn`` with the DB ``fi"""
    ...

def get_all_model_fields(model): # -> list[Unknown]:
    ...

def get_model_field(model, field_name): # -> None:
    """
    Get a ``model`` field, trav"""
    ...

def get_field_parts(model, field_name):
    """
    Get the field parts that re"""
    ...

def resolve_field(model_field, lookup_expr):
    """
    Resolves a ``lookup_expr`` """
    ...

def handle_timezone(value, is_dst=...): # -> datetime:
    ...

def verbose_field_name(model, field_name): # -> str:
    """
    Get the verbose name for a """
    ...

def verbose_lookup_expr(lookup_expr): # -> str:
    """
    Get a verbose, more humaniz"""
    ...

def label_for_filter(model, field_name, lookup_expr, exclude=...): # -> str | None:
    """
    Create a generic label suit"""
    ...

def translate_validation(error_dict): # -> ValidationError:
    """
    Translate a Django ErrorDic"""
    ...

