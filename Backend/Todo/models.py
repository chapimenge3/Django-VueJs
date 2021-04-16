from django.db import models


class Todo(models.Model):
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(blank=True, default=False)
    
    def __str__(self) -> str:
        return f'{self.description[:20]}...'

