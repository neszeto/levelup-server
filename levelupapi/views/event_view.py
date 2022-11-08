from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from levelupapi.models import Event
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer
from rest_framework.decorators import action


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
            game_id = request.query_params['game']
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
    def destroy(self, request, pk):
        """handles DELETE requests to events"""
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    #@action turns the method into a route (http://localhost:8000/events/2/signup)
    @action(methods=['post'], detail=True) #this action will accept post methods and because detail=True, the url will include pk
    def signup(self, request, pk):
        """Post request for a user to sign up for an event"""
    
        gamer = Gamer.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.gamers.add(gamer)
        return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def leave(self, request, pk):
        """delete request for user to leave an event"""

        gamer = Gamer.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.gamers.remove(gamer)

        return Response({'message': 'Gamer deleted'}, status=status.HTTP_204_NO_CONTENT)


class EventGameSerializer(serializers.ModelSerializer):
    """JSON serlizier for games on events"""
    class Meta: 
        model = Game
        fields = ('id', 'title')


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events"""
    game = EventGameSerializer(many=False)

    class Meta:
        model = Event
        fields = ('id', 'game', 'description', 'date', 'time', 'organizer')