from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    total_score = models.IntegerField(default=0)


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