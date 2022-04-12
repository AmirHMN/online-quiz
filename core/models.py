from django.core.exceptions import ValidationError
from django.db import models
from quiz.settings import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='کاربر')

    class Meta:
        verbose_name = 'پروفایل کابر'
        verbose_name_plural = 'پروفایل های کاربران'

    #
    # def correct_count(self):
    #     return SubmittedAnswer.objects.filter(user_profile=self, is_correct_answer=True).count()

    def __str__(self):
        return self.user.__str__()


class Group(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')

    class Meta:
        verbose_name = 'گروه'
        verbose_name_plural = 'گروه ها'

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField(max_length=250, verbose_name='متن سوال')
    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name='questions', verbose_name='گروه')

    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوالات'

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=250, verbose_name='متن')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', verbose_name='سوال')
    correct = models.BooleanField(default=False, verbose_name='پاسخ صحیح')

    class Meta:
        verbose_name = 'پاسخ'
        verbose_name_plural = 'پاسخ ها'

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


class SubmittedAnswer(models.Model):
    question_id = models.IntegerField(blank=True, verbose_name='آیدی سوال')
    answer_id = models.IntegerField(verbose_name='آیدی پاسخ')
    is_correct_answer = models.BooleanField(blank=True, verbose_name='پاسخ صحیح؟',
                                            help_text='آیا پاسخ داده شده صحیح است؟')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='submitted_answers',
                                     verbose_name='پروفایل کاربر')
    submitted_at = models.DateField(auto_now_add=True, verbose_name='ثبت شده در')

    def group_id(self):
        return Question.objects.get(id=self.question_id).group.pk

    def save(self, *args, **kwargs):
        answer = Answer.objects.get(id=self.answer_id)
        self.question_id = answer.question.pk
        self.is_correct_answer = answer.correct
        super(SubmittedAnswer, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_profile.__str__()

    class Meta:
        unique_together = ['user_profile', 'question_id', 'submitted_at']
        verbose_name = 'پاسخ ثبت شده'
        verbose_name_plural = 'پاسخ های ثبت شده'


class CorrectDetail(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='correct_details',
                                     verbose_name='پروفایل کاربر')
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    national_code = models.CharField(max_length=10, unique=True, verbose_name='کد ملی')
    submitted_at = models.DateField(auto_now_add=True, verbose_name='ثبت شده در')
    count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.first_name = self.user_profile.user.first_name
        self.last_name = self.user_profile.user.last_name
        self.national_code = self.user_profile.user.national_code
        self.count = SubmittedAnswer.objects.filter(submitted_at=self.submitted_at, user_profile=self.user_profile,
                                                    is_correct_answer=True).count()
        super(CorrectDetail, self).save(*args, **kwargs)


class Winner(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='کاربر')
    won_at = models.DateField(verbose_name='برنده شده در')
