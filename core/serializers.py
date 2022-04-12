from django.db import transaction
from rest_framework import serializers
from .models import Question, Answer, Group, SubmittedAnswer, UserProfile, CorrectDetail, Winner


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'correct']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'answers']


class GroupSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'title', 'questions']


class SubmitAnswerSerializer(serializers.Serializer):
    answer_id = serializers.IntegerField()

    def save(self, **kwargs):
        with transaction.atomic():
            user_profile = UserProfile.objects.get(user=self.context['request'].user)
            answer = SubmittedAnswer.objects.create(user_profile=user_profile,
                                                    answer_id=self.validated_data['answer_id'])
            return answer


class SubmittedAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmittedAnswer
        fields = ['question_id', 'answer_id', 'is_correct_answer', 'submitted_at']


class CorrectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorrectDetail
        fields = ['count', 'submitted_at']


class UserProfileSerializer(serializers.ModelSerializer):
    correct_details = CorrectDetailSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ['user_id', 'correct_details']


class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = ['user', 'won_at']
