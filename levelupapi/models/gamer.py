from django.db import models
from django.contrib.auth.models import User


class Gamer(models.Model):
    """Database model for Gamers"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)