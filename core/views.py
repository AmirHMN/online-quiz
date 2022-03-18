from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Question
from .serializers import QuestionSerializer


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_permissions(self):
        if self.action in ['list', 'destroy', 'update', 'partial_update']:
            return [IsAdminUser()]
        else:
            return [IsAuthenticated()]
