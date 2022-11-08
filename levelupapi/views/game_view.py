"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from levelupapi.models import Game, Gamer, GameType
from rest_framework.response import Response
from rest_framework import serializers, status



class GameView(ViewSet):
    """level up game view"""

    def retrieve(self, request, pk):
        """handle GET for a single game"""
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def list(self, request):
        """handle GET for all games"""
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        game_type = GameType.objects.get(pk=request.data["gameType"])

        game = Game.objects.create(
            title=request.data["title"],
            maker=request.data["maker"],
            number_of_players=request.data["numberOfPlayers"],
            skill_level=request.data["skillLevel"],
            gamer=gamer,
            game_type=game_type
        )
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def update(self, request, pk):
        """handle PUT requests for games"""

        game = Game.objects.get(pk=pk) #this creates an instance of the game and gamer is already on it so no need to change it because theres no way a client can change the value
        game.title = request.data["title"]
        game.maker = request.data["maker"]
        game.number_of_players = request.data["numberOfPlayers"]
        game.skill_level = request.data["skillLevel"]

        game_type = GameType.objects.get(pk=request.data["gameType"])
        game.game_type = game_type
        game.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """handle DELETE requests for games"""
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games"""
    class Meta:
        model = Game
        fields = ('id', 'game_type', 'title', 'maker', 'gamer', 'number_of_players', 'skill_level')
        depth = 1

