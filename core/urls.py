from django.urls import path, include
from .views import QuestionViewSet, GroupViewSet, ResultViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('group', GroupViewSet, basename='group')
router.register('result', ResultViewSet, basename='result')
group_router = routers.NestedDefaultRouter(router, 'group', lookup='group')
group_router.register('questions', QuestionViewSet, basename='question')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(group_router.urls)),
]
