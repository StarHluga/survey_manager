from django.urls import path
from .views import survey_list, survey_detail, survey_form, survey_results, survey_response

urlpatterns = [
    path('', survey_list, name='survey_list'),
    path('survey/<int:pk>/', survey_detail, name='survey_detail'),
    path('survey/<int:pk>/form/', survey_form, name='survey_form'),
    path('survey/<int:pk>/results/', survey_results, name='survey_results'),
    path('response/<int:response_id>/', survey_response, name='survey_response'),
]