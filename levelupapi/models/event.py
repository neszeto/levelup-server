from django.db import models




class Event(models.Model): 
    """Database model for Event"""
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='event_game')
    description = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    organizer = models.ForeignKey('Gamer', on_delete=models.CASCADE, related_name='event_organizer')
    gamers = models.ManyToManyField('Gamer', through='EventGamer')