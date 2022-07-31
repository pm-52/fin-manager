from rest_framework import viewsets
from rest_framework.serializers import BaseSerializer
from rest_framework.permissions import IsAuthenticated
from finance.filters import DateTimeFilter

from finance.models import FinanceCategoryConstructor, FinanceCategory, FinancialAccounting
from finance.serializers import CategoryConstructorSerializer, CategorySerializer, FinancialAccountingSerializer

# Create your views here.


class WaterfallViewSet(viewsets.ModelViewSet):
    serializer_class = FinancialAccountingSerializer
    permission_classes = [IsAuthenticated]
    filter_class = DateTimeFilter

    def get_queryset(self):
        user = self.request.user
        return FinancialAccounting.objects.filter(user=user).order_by("-created")

    def perform_create(self, serializer: BaseSerializer):
        serializer.save(user=self.request.user)


class CategoryConstructorViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryConstructorSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return FinanceCategoryConstructor.objects.filter(user=user)

    def perform_create(self, serializer: BaseSerializer):
        serializer.save(user=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FinanceCategory.objects.filter(user=user)

    def perform_create(self, serializer: BaseSerializer):
        serializer.save(user=self.request.user)
