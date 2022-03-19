from django.contrib import admin
from .models import Quiz, Question, Answer, ConfirmedAnswer


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    pass


class AnswerTabInlineAdmin(admin.TabularInline):
    model = Answer
    fields = ['text']
    min_num = 4
    max_num = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'quiz']
    inlines = [AnswerTabInlineAdmin]


@admin.register(ConfirmedAnswer)
class ConfirmedAnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['text', 'question', 'correct']
    list_editable = ['correct']
