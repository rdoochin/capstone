import datetime

from django.db import models
from django.utils import timezone

## From tutorial     ##      ##      ##      ##
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # This makes editing the sql in the terminal more readable.
    def __str__(self):
        return self.question_text

    # date-time stuff.
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # This makes editing the sql in the terminal more readable.
    def __str__(self):
        return self.question_text
##      ##      ##      ##      ##       ##      ##
