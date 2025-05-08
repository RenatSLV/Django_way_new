from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)