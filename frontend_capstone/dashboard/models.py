import datetime
from django.db import models
from django.contrib.auth.models import User


from django.utils import timezone

# Outlines the information given for each student in the database.
class Student(models.Model):
    id_num = models.IntegerField(default=0)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    class_year = models.CharField(max_length=20)
    greek_org = models.CharField(max_length=20)
    housing_building = models.CharField(max_length=20)
    club = models.CharField(max_length=20)
    last_modifed = models.DateTimeField(auto_now=True)


