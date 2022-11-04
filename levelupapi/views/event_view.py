from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from levelupapi.models import Event
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer


class EventView(ViewSet):
    """level up event view"""

    def retrieve(self, request, pk):
        """handle GET for a single event"""
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        """handle GET for all events"""
        if "game" in request.query_params: 
            game_id = request.query_params['game'][0]
            events = Event.objects.filter(game=game_id)

        else: 
            events = Event.objects.all()

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def create(self, request):
        """handles POST requests to events"""
        organizer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])
        
        event = Event.objects.create(
            description = request.data["description"],
            date = request.data["date"],
            time = request.data["time"],
            game = game,
            organizer = organizer
        )

        serializer = EventSerializer(event)
        return Response(serializer.data)

    def update(self, request, pk):
        """handles PUT request to events"""

        event = Event.objects.get(pk=pk)
        event.game = Game.objects.get(pk=request.data["game"])
        event.description = request.data["description"]
        event.date = request.data["date"]
        event.time = request.data["time"]
        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

        
class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events"""
    class Meta:
        model = Event
        fields = ('id', 'game', 'description', 'date', 'time', 'organizer')