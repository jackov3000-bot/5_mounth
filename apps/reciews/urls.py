from rest_framework.routers import DefaultRouter
from apps.reciews.views import ReviewViewSet, ReviewDetailViewSet

router = DefaultRouter()
router.register('', ReviewViewSet, basename='review-list-create')
router.register('detail', ReviewDetailViewSet, basename='review-detail')

urlpatterns = router.urls