from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.generics import ListAPIView,ListCreateAPIView
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from .models import Group, Question, UserProfile, SubmittedAnswer, Winner
from .serializers import QuestionSerializer, GroupSerializer, SubmitAnswerSerializer, UserProfileSerializer, \
    WinnerSerializer
import datetime
from rest_framework.permissions import *


class GroupViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'head', 'options']

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_queryset(self):
        answers = SubmittedAnswer.objects.filter(user_profile__user=self.request.user)
        if self.action == 'retrieve':
            flag = False
            group_id_list = []
            for answer in answers:
                group_id_list.append(answer.group_id())
                print(answer.submitted_at, datetime.date.today())
                if answer.submitted_at == datetime.date.today():
                    flag = True
                    break
            if int(self.kwargs['pk']) in group_id_list and flag:
                raise PermissionDenied("شما قبلا به سوال این گروه پاسخ داده اید!")
        return Group.objects.all()

    serializer_class = GroupSerializer


class QuestionViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_queryset(self):
        return Question.objects.filter(group_id=self.kwargs['group_pk'])

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SubmitAnswerSerializer
        return QuestionSerializer


class ResultViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return UserProfile.objects.all().order_by('correct_details__count', 'correct_details__submitted_at')

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser()]
        return [IsAuthenticated()]

    @action(detail=False, methods=['get'])
    def me(self, request):
        user = request.user
        user_profile = UserProfile.objects.get(user=user)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

    serializer_class = UserProfileSerializer


class WinnerView(ListCreateAPIView):
    queryset = Winner.objects.all()
    serializer_class = WinnerSerializer
