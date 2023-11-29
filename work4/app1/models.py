
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
  email = models.EmailField()
  phone = models.CharField(max_length=10)