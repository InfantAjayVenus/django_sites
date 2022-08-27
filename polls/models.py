from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=300)
    date_published = models.DateTimeField()
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)