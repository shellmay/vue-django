from django.db import models

# Create your models here.
from django.db import models


class Login(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Deparment(models.Model):
    question = models.ForeignKey(Login, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
