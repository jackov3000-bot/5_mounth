from django.urls import path

from apps.library.views import PurchaseGameViewSet

purchase_view = PurchaseGameViewSet.as_view({
    'post': 'create'
})

urlpatterns = [
    path('purchase/<int:game_id>/', purchase_view, name='purchase-game'),
]