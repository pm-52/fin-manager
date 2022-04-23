from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    username = models.TextField(max_length=30, unique=True)
    password = models.TextField(max_length=30)

USERNAME_FIELD = 'username'
REQUIRED_FIELDS = ['email', 'password']

def __str__(self):
    return self.username
