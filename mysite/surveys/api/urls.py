from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyViewSet, QuestionViewSet, ResponseViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'responses', ResponseViewSet)
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
# mysite/surveys/api/urls.py
# This file sets up the API endpoints for the surveys application using Django REST Framework.