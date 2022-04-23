"""
This type stub file was generated by pyright.
"""

from collections import OrderedDict
from typing import Any, Iterable, List, Tuple, Type
from django.db.models.expressions import Expression
from django.db.models.fields import Field
from django.db.models.lookups import BuiltinLookup, Exact, GreaterThan, GreaterThanOrEqual, In, IsNull, LessThan, LessThanOrEqual

class MultiColSource:
    alias: str
    field: Field[Any, Any]
    sources: Tuple[Field[Any, Any], Field[Any, Any]]
    targets: Tuple[Field[Any, Any], Field[Any, Any]]
    contains_aggregate: bool = ...
    output_field: Field[Any, Any] = ...
    def __init__(self, alias: str, targets: Tuple[Field[Any, Any], Field[Any, Any]], sources: Tuple[Field[Any, Any], Field[Any, Any]], field: Field[Any, Any]) -> None:
        ...
    
    def relabeled_clone(self, relabels: OrderedDict[Any, Any]) -> MultiColSource:
        ...
    
    def get_lookup(self, lookup: str) -> Type[BuiltinLookup[Any]]:
        ...
    


def get_normalized_value(value: Any, lhs: Expression) -> Tuple[None]:
    ...

class RelatedIn(In):
    bilateral_transforms: List[Any]
    lhs: Expression
    rhs: Any = ...
    def get_prep_lookup(self) -> Iterable[Any]:
        ...
    


class RelatedLookupMixin:
    rhs: Any = ...
    def get_prep_lookup(self) -> Any:
        ...
    


class RelatedExact(RelatedLookupMixin, Exact):
    ...


class RelatedLessThan(RelatedLookupMixin, LessThan[Any]):
    ...


class RelatedGreaterThan(RelatedLookupMixin, GreaterThan):
    ...


class RelatedGreaterThanOrEqual(RelatedLookupMixin, GreaterThanOrEqual[Any]):
    ...


class RelatedLessThanOrEqual(RelatedLookupMixin, LessThanOrEqual):
    ...


class RelatedIsNull(RelatedLookupMixin, IsNull):
    ...

