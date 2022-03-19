from rest_framework import viewsets
from .models import Quiz, Question
from .serializers import QuestionSerializer, QuizSerializer, SubmitAnswerSerializer


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
