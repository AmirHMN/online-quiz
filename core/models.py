from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=250)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

