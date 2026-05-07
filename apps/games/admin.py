from django.contrib import admin

from apps.games.models import Games, Genre

admin.site.register(Games)
admin.site.register(Genre)

# Register your models here.
