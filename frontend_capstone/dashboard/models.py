#!/rebekahdoochin/senior_year/capstone/capstone/frontend_capstone/dashboard python
import datetime
from django.db import models
from django.contrib.auth.models import User     # Pretty sure we need this. 
# import numpy as np
# from random import randint

from django.utils import timezone

class Student(models.Model):
    id_num = models.IntegerField(default=0)         #should maybe be the input?
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    # phone_number = models.CharField(max_length=20)
    # gender = models.CharField(max_length=20)
    class_year = models.CharField(max_length=20)
    greek_org = models.CharField(max_length=20)
    housing_building = models.CharField(max_length=20)
    # current_class = models.CharField(max_length=20)
    club = models.CharField(max_length=20)            #models.expressionlist ? 
    # sport = models.CharField(max_length=20)
    last_modifed = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title


#sources:
# https://www.youtube.com/watch?v=QUXvqfN1ENM

