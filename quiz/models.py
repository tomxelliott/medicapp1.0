from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    date_joined = models.DateTimeField(default=datetime.now, blank=True)
    total_score = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username


class Topic(models.Model):
    topic_text = models.CharField(max_length=20)

    def __str__(self):
        return self.topic_text


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=400)

    def __str__(self):
        return self.question_text

    def get_topic(self):
        return str(self.topic)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text