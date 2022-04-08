from typing import Any
from rest_framework import serializers

from finance.models import FinanceCategory, FinancialAccounting


class FinancialAccountingSerializer(serializers.ModelSerializer):
    """
    Financial Accounting Serializer
    """

    category = serializers.PrimaryKeyRelatedField(
        many=False, queryset=FinanceCategory.objects
    )

    class Meta:
        model = FinancialAccounting
        fields = ["id", "category", "value", "created"]


class CategorySerializer(serializers.ModelSerializer):
    """
    Finance category serializer
    """

    class Meta:
        model = FinanceCategory
        fields = ["id", "title"]
