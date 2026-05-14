from django.db import models
from apps.user.models import User
from apps.games.models import Games

class Library(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='library'
    )
    game = models.ForeignKey(
        Games,
        on_delete=models.CASCADE,
        related_name='library'
    )
    purchased_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.user.username} - {self.game.title}"
    
    class Meta:
        unique_together = ('user', 'game')
        verbose_name = 'Библиотека'
        verbose_name_plural = 'Библиотеки'

# Create your models here.
