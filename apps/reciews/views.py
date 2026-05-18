from rest_framework.viewsets import ModelViewSet
from apps.reciews.models import Review
from apps.reciews.serializers import ReviewSerializer

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Create your views here.
