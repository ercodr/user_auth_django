from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(models.Model):
    username = models.CharField(max_length=150)
    password = models.TextField()