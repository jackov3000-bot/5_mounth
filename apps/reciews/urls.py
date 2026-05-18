from rest_framework.routers import DefaultRouter
from apps.reciews.views import ReviewViewSet

router = DefaultRouter()
router.register('reviews', ReviewViewSet, basename='review')

urlpatterns = router.urls