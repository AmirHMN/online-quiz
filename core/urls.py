from django.urls import path, include
from .views import QuestionView

from rest_framework import routers
router = routers.DefaultRouter()
router.register('questions', QuestionView, basename='questions')

urlpatterns = [
    path('', include(router.urls))
]
