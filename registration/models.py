from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_user_model(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)
    address =  models.TextField(blank=True, null=True)