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


class ConfirmedAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmedAnswer
        fields = ['question_id', 'answer_id', 'correct_answer']


class UserProfileSerializer(serializers.ModelSerializer):
    correct_count = serializers.SerializerMethodField()
    confirmed_answers = ConfirmedAnswerSerializer(many=True)

    def get_correct_count(self, answer):
        return ConfirmedAnswer.objects.filter(user_profile__user=self.context['request'].user,
                                              correct_answer=True).count()

    class Meta:
        model = ConfirmedAnswer
        fields = ['confirmed_answers', 'correct_count']
