from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from apps.reciews.models import Review
from apps.reciews.serializers import ReviewSerializer

class ReviewViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
# Create your views here.

