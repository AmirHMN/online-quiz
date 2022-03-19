from django.core.exceptions import ValidationError
from django.db import models
from quiz import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.__str__()


class Quiz(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField(max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT, related_name='questions')

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=250)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
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


class ConfirmedAnswer(models.Model):
    question_id = models.IntegerField(blank=True)
    answer_id = models.IntegerField()
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.question_id = Answer.objects.get(id=self.answer_id).question.pk
        super(ConfirmedAnswer, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_profile.__str__() + ' , ' + Answer.objects.get(id=self.answer_id).__str__()

    class Meta:
        unique_together = ['user_profile', 'question_id']
