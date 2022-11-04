
from django.db import models


class EventGamer(models.Model):
    """Database model for EventGamer"""
    gamer = models.ForeignKey('Gamer', on_delete=models.CASCADE, related_name='attending_gamer')
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='event_attending')