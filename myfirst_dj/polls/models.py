import datetime

from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.


class Question(models.Model):

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?'
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):

    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Person(models.Model):

    def __str__(self):
        return self.first_name
    db_table = 'user_info'
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    second_name = models.CharField("person's secod name", max_length=30)
