from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Quiz, Question
from .serializers import QuestionSerializer, QuizSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        print(self.kwargs)
        return Question.objects.filter(quiz_id=self.kwargs['quiz_pk'])

    serializer_class = QuestionSerializer

    def get_permissions(self):
        if self.action in ['list', 'destroy', 'update', 'partial_update']:
            return [IsAdminUser()]
        else:
            return [IsAuthenticated()]
