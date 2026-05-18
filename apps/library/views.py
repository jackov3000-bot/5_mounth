from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.library.models import Library
from apps.games.models import Games
from apps.library.serializers import LibrarySerializer

class PurchaseGameViewSet(mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = LibrarySerializer
    Permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        game_id = kwargs.get('game_id')

        game = Games.objects.get(id=game_id)

        if not game:
            return Response(
                {"error": "Игра не найдена."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        aready_purchased = Library.objects.filter(
            user=request.user,
            game=game
        ).exists()

        if aready_purchased:
            return Response(
                {"error": "Вы уже приобрели эту игру."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        library = Library.objects.create(
            user=request.user,
            game=game
        )

        return Response(
            {"message": "Игра успешно приобретена."},
            status=status.HTTP_201_CREATED
        )
        



# Create your views here.
