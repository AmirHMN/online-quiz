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

    def save(self, *args, **kwargs):
        answers = Answer.objects.filter(question=self.question)
        flag = False
        for answer in answers:
            if answer.correct:
                flag = True
                break
        if flag and self.correct:
            raise ValidationError('Question can not have more than 1 correct answer')
        super(Answer, self).save(*args, **kwargs)
