from django.db import models



class Game(models.Model): 
    """Database mode for game"""
    game_type = models.ForeignKey('GameType', on_delete=models.CASCADE, related_name='games_by_type')
    title = models.CharField(max_length=55)
    maker = models.CharField(max_length=55)
    gamer = models.ForeignKey('Gamer', on_delete=models.CASCADE, related_name='created_games')
    number_of_players = models.PositiveIntegerField(default=0)
    skill_level = models.IntegerField(default=0)