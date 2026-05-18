from rest_framework import serializers
from apps.games.models import Games
from apps.reciews.models import Review




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'