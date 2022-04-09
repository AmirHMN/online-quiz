from .models import UserProfile
from django.dispatch import receiver
from django.db.models.signals import post_save
from quiz.settings import settings
from core.models import SubmittedAnswer, CorrectDetail


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile_for_new_user(sender, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=kwargs['instance'])


@receiver(post_save, sender=SubmittedAnswer)
def create_correct_detail_after_submit_answer(sender, **kwargs):
    answer = kwargs['instance']
    detail, created = CorrectDetail.objects.get_or_create(user_profile=answer.user_profile,
                                                          submitted_at=answer.submitted_at)
    if not created:
        detail.count += 1
        detail.save()
