from django.db import models
from django.contrib.auth.models import AbstractUser

class Post(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)