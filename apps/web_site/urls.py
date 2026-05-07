from django.urls import path
from .views import WelcomeAPIView, AboutAPIView, ContactAPIView

urlpatterns = [
    path('welcome/', WelcomeAPIView.as_view()),
    path('about/', AboutAPIView.as_view()),
    path('contacts/', ContactAPIView.as_view()),
]