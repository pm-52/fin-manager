from finance.models import FinancialAccounting
import django_filters


class DateTimeFilter(django_filters.FilterSet):
    created_gte = django_filters.DateTimeFilter(field_name="created", lookup_expr="gte")
    created_lte = django_filters.DateTimeFilter(field_name="created", lookup_expr="lte")

    class Meta:
        model = FinancialAccounting
        fields = ["created"]
