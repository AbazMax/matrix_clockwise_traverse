import re
from django.core.exceptions import ValidationError
from django.db import models

from .matrix_convertation import get_values

class MatrixField(models.TextField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    description = "A field for storing matrices"

    def validate_matrix_format(self, matrix):
        # format validation
        matrix = matrix.replace('\r', '').strip().split('\n')
        for row in matrix[::2]:
            pattern = r'^[+-]*$'
            if not re.search(pattern, row):
                raise ValidationError("Invalid matrix format")
            if not row.startswith('+-') or not row.endswith('-+'):
                raise ValidationError("Invalid matrix format")
        for row in matrix[1::2]:
            pattern = r'^[\d |]*$'
            if not re.search(pattern, row):
                raise ValidationError("Invalid matrix format") 
            if not row.startswith('| ') or not row.endswith(' |'):
                raise ValidationError("Invalid matrix format")
        
    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        self.validate_matrix_format(value)

    def from_db_value(self, value, expression, connection):
        self.validate_matrix_format(value)
        return value

    def to_python(self, value):
        return value

    def get_prep_value(self, value):
        return value
    
    
class Matrix(models.Model):
    """Model for save input matrices"""
    
    input_matrix = MatrixField()
    list_of_values = models.TextField(default="", blank=True, null=True)

    def get_list(self):
        return get_values(self.input_matrix)

    def save(self, *args, **kwargs):
        if not self.list_of_values:
            self.list_of_values = self.get_list()
        super().save(*args, **kwargs)
        # updating list_of_values after changing input_matrix
        self.list_of_values = self.get_list()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'matrices'

    def __str__(self) -> str:
        return f'{self.input_matrix}'
    
 