import random
from random import randint
import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker
from dashboard.models import Student

# Creating pools of information for the phony data to be generated from.
CLUBS = [
    "Book club", "Cycling", "Tennis Club", "Soccer Club", "Rowing",
    "Karate", "Baseball Club", "Comedy Club", "Feminism", "Dance Team",
    "Running", "Walking", "Cookies and Code", "Puppies Club", "Community Service",
    "Club 1", "Club 2", "Club 3", "Club 4", "Club 5", "Club 6", "Club 7",
    "Club 8", "Club 9", "Club 10", "Club 11", "Club 12", "Club 13", "Club 14",
    "Club 15", "Club 16", "Club 17"
]
YEAR = ["Freshman", "Sophmore", "Junior", "Senior", "Graduate"]
GREEK = [
    "AEPhi", "AEPi", "ZBT", "Pi Phi", "Chi O", "Theta", "Phi Mu", "Kappa",
         "Zeta Psi", "KSig", "SigEp"
]
DORM = [
    "Sharp 1", "Sharp 2", "Irby 345", "Phelps 233", "Mayer 420", "Butler 5",
        "Sharp 4", "Monroe 2", "Irby 385", "Aron 233", "Mayer 400", "Aron 439"
]

# Functions to grab the randomized data from the lists. 
class Provider(faker.providers.BaseProvider):
    def student_clubs(self):
        return self.random_element(CLUBS)

    def student_year(self):
        return self.random_element(YEAR)

    def student_greek(self):
        return self.random_element(GREEK)

    def student_dorm(self):
        return self.random_element(DORM)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):      

        fake = Faker()
        fake.add_provider(Provider)

        for _ in range(100):            # Stores the random data in temporary variables.
            c = fake.student_clubs()
            y = fake.student_year()
            g = fake.student_greek()
            d = fake.student_dorm()

            id_num = randint(100000000, 999999999)
            first = fake.first_name()
            last = fake.last_name()
            email = fake.free_email()

            Student.objects.create(     # Creates a student with the variables.
                id_num=id_num,
                first_name=first,
                last_name=last,
                email=email,
                class_year=y,
                housing_building=d,
                club=c,
                greek_org=g,
            )

        check_category = Student.objects.all().count()
        self.stdout.write(self.style.SUCCESS(
            f"Number of categories: {check_category}"))
