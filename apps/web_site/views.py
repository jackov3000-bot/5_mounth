from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class WelcomeAPIView(APIView):
    def get(self, request):
        return Response({"message": "Привет!"})

class AboutAPIView(APIView):
    def get(self, request):
        return Response({"about": "О нас"})

class ContactAPIView(APIView):
    def get(self, request):
        return Response({"contacts": "Контакты"})

# Create your views here.
