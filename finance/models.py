from binhex import FInfo
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class FinanceCategory(models.Model):
    """
    Custom category of expenses/income
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()

    class Meta:
        unique_together = ("user", "title")


class FinanceCategoryConstructor(models.Model):
    """
    Constructor for user's set of categories
    """

    # id = models.IntegerField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(FinanceCategory, null=True, on_delete=models.SET_NULL)
    type = models.IntegerField()
    color = models.CharField(max_length=10)
    emoji = models.CharField(max_length=10)
    


class FinancialAccounting(models.Model):
    """
    Expenses/income row of user
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(FinanceCategory, null=True, on_delete=models.SET_NULL)
    value = models.DecimalField(decimal_places=2, max_digits=15)
    created = models.DateTimeField(auto_now_add=True)
