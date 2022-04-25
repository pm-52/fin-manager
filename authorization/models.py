from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    username = models.TextField(max_length=30, unique=True)
    email = models.EmailField(max_length=60, unique=True)

USERNAME_FIELD = 'username'
REQUIRED_FIELDS = ['username', 'email']

def __str__(self):
    return self.username
