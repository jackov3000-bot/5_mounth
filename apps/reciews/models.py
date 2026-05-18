from django.db import models
from apps.games.models import Games  

class Review(models.Model):
    game = models.ForeignKey(
        Games, 
        on_delete=models.CASCADE, 
        related_name='reviews'
    )
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Отзыв на {self.game.title} - {self.rating}/5"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'