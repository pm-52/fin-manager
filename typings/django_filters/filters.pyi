"""
This type stub file was generated by pyright.
"""

from django import forms
from .fields import BaseCSVField, BaseRangeField, ChoiceField, DateRangeField, DateTimeRangeField, IsoDateTimeField, IsoDateTimeRangeField, LookupChoiceField, ModelChoiceField, ModelMultipleChoiceField, MultipleChoiceField, RangeField, TimeRangeField

__all__ = ['AllValuesFilter', 'AllValuesMultipleFilter', 'BaseCSVFilter', 'BaseInFilter', 'BaseRangeFilter', 'BooleanFilter', 'CharFilter', 'ChoiceFilter', 'DateFilter', 'DateFromToRangeFilter', 'DateRangeFilter', 'DateTimeFilter', 'DateTimeFromToRangeFilter', 'DurationFilter', 'Filter', 'IsoDateTimeFilter', 'IsoDateTimeFromToRangeFilter', 'LookupChoiceFilter', 'ModelChoiceFilter', 'ModelMultipleChoiceFilter', 'MultipleChoiceFilter', 'NumberFilter', 'NumericRangeFilter', 'OrderingFilter', 'RangeFilter', 'TimeFilter', 'TimeRangeFilter', 'TypedChoiceFilter', 'TypedMultipleChoiceFilter', 'UUIDFilter']
class Filter:
    creation_counter = ...
    field_class = forms.Field
    def __init__(self, field_name=..., lookup_expr=..., *, label=..., method=..., distinct=..., exclude=..., **kwargs) -> None:
        ...
    
    def get_method(self, qs):
        """Return filter method based on wh"""
        ...
    
    def method(): # -> dict[str, Any]:
        """
        Filter method needs to """
        ...
    
    method = ...
    def label(): # -> dict[str, Any]:
        ...
    
    label = ...
    @property
    def field(self): # -> field_class:
        ...
    
    def filter(self, qs, value):
        ...
    


class CharFilter(Filter):
    field_class = forms.CharField


class BooleanFilter(Filter):
    field_class = forms.NullBooleanField


class ChoiceFilter(Filter):
    field_class = ChoiceField
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def filter(self, qs, value):
        ...
    


class TypedChoiceFilter(Filter):
    field_class = forms.TypedChoiceField


class UUIDFilter(Filter):
    field_class = forms.UUIDField


class MultipleChoiceFilter(Filter):
    """
    This filter performs OR(by """
    field_class = MultipleChoiceField
    always_filter = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def is_noop(self, qs, value): # -> bool:
        """
        Return `True` to short-"""
        ...
    
    def filter(self, qs, value):
        ...
    
    def get_filter_predicate(self, v): # -> dict[str | Unknown, Any] | dict[str | Unknown, Unknown]:
        ...
    


class TypedMultipleChoiceFilter(MultipleChoiceFilter):
    field_class = forms.TypedMultipleChoiceField


class DateFilter(Filter):
    field_class = forms.DateField


class DateTimeFilter(Filter):
    field_class = forms.DateTimeField


class IsoDateTimeFilter(DateTimeFilter):
    """
    Uses IsoDateTimeField to su"""
    field_class = IsoDateTimeField


class TimeFilter(Filter):
    field_class = forms.TimeField


class DurationFilter(Filter):
    field_class = forms.DurationField


class QuerySetRequestMixin:
    """
    Add callable functionality """
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def get_request(self): # -> None:
        ...
    
    def get_queryset(self, request): # -> None:
        ...
    
    @property
    def field(self):
        ...
    


class ModelChoiceFilter(QuerySetRequestMixin, ChoiceFilter):
    field_class = ModelChoiceField
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class ModelMultipleChoiceFilter(QuerySetRequestMixin, MultipleChoiceFilter):
    field_class = ModelMultipleChoiceField


class NumberFilter(Filter):
    field_class = forms.DecimalField
    def get_max_validator(self): # -> MaxValueValidator:
        """
        Return a MaxValueValida"""
        ...
    
    @property
    def field(self): # -> field_class:
        ...
    


class NumericRangeFilter(Filter):
    field_class = RangeField
    def filter(self, qs, value):
        ...
    


class RangeFilter(Filter):
    field_class = RangeField
    def filter(self, qs, value):
        ...
    


class DateRangeFilter(ChoiceFilter):
    choices = ...
    filters = ...
    def __init__(self, choices=..., filters=..., *args, **kwargs) -> None:
        ...
    
    def filter(self, qs, value):
        ...
    


class DateFromToRangeFilter(RangeFilter):
    field_class = DateRangeField


class DateTimeFromToRangeFilter(RangeFilter):
    field_class = DateTimeRangeField


class IsoDateTimeFromToRangeFilter(RangeFilter):
    field_class = IsoDateTimeRangeField


class TimeRangeFilter(RangeFilter):
    field_class = TimeRangeField


class AllValuesFilter(ChoiceFilter):
    @property
    def field(self): # -> field_class:
        ...
    


class AllValuesMultipleFilter(MultipleChoiceFilter):
    @property
    def field(self): # -> field_class:
        ...
    


class BaseCSVFilter(Filter):
    """
    Base class for CSV type fil"""
    base_field_class = BaseCSVField
    def __init__(self, *args, **kwargs) -> None:
        class ConcreteCSVField(self.base_field_class, self.field_class):
            ...
        
        
    


class BaseInFilter(BaseCSVFilter):
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class BaseRangeFilter(BaseCSVFilter):
    base_field_class = BaseRangeField
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class LookupChoiceFilter(Filter):
    """
    A combined filter that allo"""
    field_class = ...
    outer_class = LookupChoiceField
    def __init__(self, field_name=..., lookup_choices=..., field_class=..., **kwargs) -> None:
        ...
    
    @classmethod
    def normalize_lookup(cls, lookup): # -> tuple[str, str] | tuple[Unknown, Unknown]:
        """
        Normalize the lookup in"""
        ...
    
    def get_lookup_choices(self): # -> list[tuple[str, str] | tuple[Unknown, Unknown]]:
        """
        Get the lookup choices """
        ...
    
    @property
    def field(self): # -> outer_class:
        ...
    
    def filter(self, qs, lookup):
        ...
    


class OrderingFilter(BaseCSVFilter, ChoiceFilter):
    """
    Enable queryset ordering. A"""
    descending_fmt = ...
    def __init__(self, *args, **kwargs) -> None:
        """
        ``fields`` may be eithe"""
        ...
    
    def get_ordering_value(self, param): # -> str:
        ...
    
    def filter(self, qs, value):
        ...
    
    @classmethod
    def normalize_fields(cls, fields): # -> OrderedDict[Unknown, Unknown] | OrderedDict[str, str]:
        """
        Normalize the fields in"""
        ...
    
    def build_choices(self, fields, labels): # -> list[tuple[Unknown, Unknown]]:
        ...
    


class FilterMethod:
    """
    This helper is used to over"""
    def __init__(self, filter_instance) -> None:
        ...
    
    def __call__(self, qs, value): # -> Any:
        ...
    
    @property
    def method(self): # -> Any:
        """
        Resolve the method on t"""
        ...
    

