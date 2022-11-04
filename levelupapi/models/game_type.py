from django.db import models

class GameType(models.Model):
    """Database model for GameType"""
    label = models.CharField(max_length=55)