from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text



