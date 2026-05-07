from django.urls import path

from apps.games.views import GamesDetailAPIView, GamesListAPIView, GenreListAPIView

urlpatterns = [
    path("list-games", GamesListAPIView.as_view(), name="list-games"),
    path("list-genres", GenreListAPIView.as_view(), name="list-genres"),
    path("detail-games/<int:pk>", GamesDetailAPIView.as_view(), name="detail-games"),
]