from rest_framework import serializers

from apps.games.models import Genre, Games

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'slug']

class GamesSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Games
        fields = [
            "id", 
            'title', "description", "genre",
            "price", "image", "rating", "developer",
            "release_data", "created_at"
        ]