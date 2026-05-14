from django.urls import path

from apps.games.views import GameListAPIView, GenreAPIView, GamesDetailAPIView

urlpatterns = [
    path("list-games", GameListAPIView.as_view(), name="list-game"),
    path("list-genre", GenreAPIView.as_view(), name="list-genre"),
    path("games/<int:id>/", GamesDetailAPIView.as_view(), name="detail-games"),
]