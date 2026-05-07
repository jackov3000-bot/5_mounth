from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from apps.games.models import Games, Genre
from apps.games.serializers import GamesSerializer, GenreSerializer

from apps.filters import GamesFilter
from apps.paginations import GamesPagination

class GamesListAPIView(ListCreateAPIView):
    queryset = Games.objects.select_related('genre').all()
    serializer_class = GamesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]

    search_fields = ['title']
    filterset_class = GamesFilter
    pagination_class = GamesPagination

class GamesDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.select_related('genre').all()
    serializer_class = GamesSerializer
    lookup_field = "id"

class GenreListAPIView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer