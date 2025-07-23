from django.shortcuts import render, get_object_or_404
from .models import Survey

# Create your views here.
def survey_list(request):
    surveys = Survey.objects.all()
    return render(request, 'surveys/survey_list.html', {'surveys': surveys})

def survey_detail(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    return render(request, 'surveys/survey_detail.html', {'survey': survey})

def survey_form(request, pk):
   survey = get_object_or_404(Survey, pk=pk)
   return render(request, 'surveys/survey_form.html', {'survey': survey})

def survey_results(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    return render(request, 'surveys/survey_results.html', {'survey': survey})

def survey_response(request):
    return render(request, 'surveys/survey_response.html')