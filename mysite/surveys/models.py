from django.db import models

# Create your models here.
class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=200)

class Response(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='responses')
    submitted_at = models.DateTimeField(auto_now_add=True)
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.ForeignKey(Response, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField(blank=True, null=True)
