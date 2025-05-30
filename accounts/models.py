from django.db import models
from django.contrib.auth.models import AbstractUser
from .constrants import USER_TYPE_CHOICES
# Create your models here.


class CustomUser(AbstractUser):
   user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)