from django.contrib import admin
from .models import Group, Question, Answer, SubmittedAnswer


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


class AnswerTabInlineAdmin(admin.TabularInline):
    model = Answer
    fields = ['text', 'correct']
    min_num = 4
    max_num = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'group']
    inlines = [AnswerTabInlineAdmin]


@admin.register(SubmittedAnswer)
class SubmittedAnswerAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'group_id', 'question_id', 'answer_id', 'submitted_at']
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['text', 'question', 'correct']
    list_editable = ['correct']
