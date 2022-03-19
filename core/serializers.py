from django.db import transaction
from rest_framework import serializers
from .models import Question, Answer, Quiz, ConfirmedAnswer, UserProfile


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'correct']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['text', 'answers']


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['title', 'questions']


class SubmitAnswerSerializer(serializers.Serializer):
    answer_id = serializers.IntegerField()

    def save(self, **kwargs):
        with transaction.atomic():
            user_profile = UserProfile.objects.get(user=self.context['request'].user)
            answer = ConfirmedAnswer.objects.create(user_profile=user_profile,
                                                    answer_id=self.validated_data['answer_id'])
            return answer
