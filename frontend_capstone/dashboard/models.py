#!/rebekahdoochin/senior_year/capstone/capstone/frontend_capstone/dashboard python
import datetime
from django.db import models
from django.contrib.auth.models import User     # Pretty sure we need this. 

from django.utils import timezone
# from django_faker import Faker
# populator = Faker.getPopulator()

##
##      Going to use the classes here to create a table in the database. Student profiles
##      should not be created here. 
##

## From tutorial     ##      ##      ##      ## not used rn
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

class Student(models.Model):
    id_num = models.IntegerField(default=0)         #should maybe be the input?
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    greek_org = models.CharField(max_length=20)
    class_year = models.IntegerField(default=0)
    housing_building = models.CharField(max_length=20)
    housing_num = models.CharField(max_length=20)
    club = models.CharField(max_length=20)            #models.expressionlist ? 
    sport = models.CharField(max_length=20)
    current_class = models.CharField(max_length=20)   #This should be a course number
    last_modifed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
