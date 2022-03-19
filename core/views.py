from rest_framework import viewsets
from .models import Quiz, Question, UserProfile, ConfirmedAnswer
from .serializers import QuestionSerializer, QuizSerializer, SubmitAnswerSerializer, ConfirmedAnswerSerializer, \
    UserProfileSerializer
from rest_framework.generics import ListAPIView


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Question.objects.filter(quiz_id=self.kwargs['quiz_pk'])

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SubmitAnswerSerializer
        return QuestionSerializer


class ResultView(ListAPIView):
    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    serializer_class = UserProfileSerializer
