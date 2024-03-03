from django.db import models

class Matrix(models.Model):
    """Model for save input matrices"""
    input_matrix = models.TextField()

    class Meta:
        verbose_name_plural = 'matrices'

    def __str__(self) -> str:
        return f'{self.input_matrix}'