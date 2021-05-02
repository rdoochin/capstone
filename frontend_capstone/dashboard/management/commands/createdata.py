import random
import numpy as np
import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker
from dashboard.models import Student

# Use python manage.py createdata to generate phony data.

CLUBS = [
    np.nan, "Book club", "Cycling", "Tennis Club", "Soccer Club", "Rowing",
    "Karate", "Baseball Club", "Comedy Club", "Feminism", "Dance Team",
    "Running", "Walking", "Cookies and Code", "Puppies Club", "Community Service",
    "Club 1", "Club 2", "Club 3", "Club 4", "Club 5", "Club 6", "Club 7",
    "Club 8", "Club 9", "Club 10", "Club 11", "Club 12", "Club 13", "Club 14",
    "Club 15", "Club 16", "Club 17"
]
YEAR = ["Freshman", "Sophmore", "Junior", "Senior", "Graduate"]
GREEK = [
    np.nan, "AEPhi", "AEPi", "ZBT", "Pi Phi", "Chi O", "Theta", "Phi Mu", "Kappa",
         "Zeta Psi", "KSig", "SigEp"
]
DORM = [
    "Sharp 1", "Sharp 2", "Irby 345", "Phelps 233", "Mayer 420", "Butler 5",
        "Sharp 4", "Monroe 2", "Irby 385", "Aron 233", "Mayer 400", "Aron 439"
]


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
    help = "Command information"

    def handle(self, *args, **kwargs):      

        fake = Faker()
        fake.add_provider(Provider)

        # for _ in range(15):
        #     c = fake.unique.student_clubs()
        #     Student.objects.create(name=d, slug=d)

        # for _ in range(15):
        #     e = fake.unique.ecommerce_products()
        #     Student.objects.create(name=e)

        for _ in range(100):
            c = fake.unique.student_clubs()
            y = fake.unique.student_year()
            g = fake.unique.student_greek()
            d = fake.unique.student_dorm()

            id_num = random(100000000, 999999999)
            first = fake.first_name()
            last = fake.last_name()
            email = fake.free_email()

            # pt = fake.text(max_nb_chars=30)
            # cid = random.randint(1, 15)
            # ptid = random.randint(1, 15)
            Student.objects.create(
                id_number=id_num,
                first_name=first,
                last_name=last,
                email=email,
                year=y,
                dorm=d,
                clubs=c,
                greek=g,
            )

        # for i in range(1, 16):
        #     ProductImage.objects.create(
        #         product_id=i, alt_text=fake.text(max_nb_chars=30), is_feature=True)

        check_category = Student.objects.all().count()
        self.stdout.write(self.style.SUCCESS(
            f"Number of categories: {check_category}"))
