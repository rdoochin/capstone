# setup_test_data.py
import random

from django.db import transaction
from django.core.management.base import BaseCommand

from dashboard.models import Student
from dashboard.dummy_data import StudentFactory

NUM_STUDENTS = 100
# NUM_CLUBS = 10
# NUM_THREADS = 12
# COMMENTS_PER_THREAD = 25
# USERS_PER_CLUB = 8


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Student]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the users
        people = []
        for _ in range(NUM_STUDENTS):
            person = StudentFactory()
            people.append(person)

        # # Add some users to clubs
        # for _ in range(NUM_CLUBS):
        #     club = ClubFactory()
        #     members = random.choices(
        #         people,
        #         k=USERS_PER_CLUB
        #     )
        #     club.user.add(*members)

        # # Create all the threads
        # for _ in range(NUM_THREADS):
        #     creator = random.choice(people)
        #     thread = ThreadFactory(creator=creator)
        #     # Create comments for each thread
        #     for _ in range(COMMENTS_PER_THREAD):
        #         commentor = random.choice(people)
        #         CommentFactory(
        #             user=commentor,
        #             thread=thread
        #         )
