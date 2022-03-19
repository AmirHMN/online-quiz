from django.urls import path, include
from .views import QuestionViewSet, QuizViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('quiz', QuizViewSet, basename='quiz')
quiz_router = routers.NestedDefaultRouter(router, 'quiz', lookup='quiz')
quiz_router.register('questions', QuestionViewSet, basename='question')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(quiz_router.urls))
]
