# From our Jupyter Notebook. 
import pandas as pd
import numpy as np
import os
import random
import matplotlib.pyplot as plt
import pickle
import time
from faker import Faker
from random import randint

from .models import Student         #Getting our Student model.

from django_seed import Seed        #START HERE!!!!!!!

randint(100, 999)
fake = Faker()


def faker_categorical(num=1, seed=None):
    """
    """
    np.random.seed(seed)
    fake.seed_instance(seed)

    output = [
        {
            "Student ID": randint(100000000, 999999999),
            "Name": fake.last_name(),
            "Email": fake.free_email(),
            "Phone Number": randint(1000000000, 9999999999),
            "Gender": np.random.choice(["M", "F", "Not Specified"], p=[0.3, 0.6, 0.1]),
            "Year": np.random.choice(["Freshman", "Sophmore", "Junior", "Senior", "Graduate"]),
            "Greek": np.random.choice([np.nan, "AEPhi", "AEPi", "ZBT", "Pi Phi", "Chi O", "Theta", "Phi Mu", "Kappa",
                                       "Zeta Psi", "KSig", "SigEp"]),
            "Dorm": np.random.choice(["Sharp 1", "Sharp 2", "Irby 345", "Phelps 233", "Mayer 420", "Butler 5",
                                      "Sharp 4", "Monroe 2", "Irby 385", "Aron 233", "Mayer 400", "Aron 439"]),
            "In_Person_Class": np.random.choice(["Math", "Finance", np.nan], p=[0.3, 0.6, 0.1]),
            "Clubs": np.random.choice([np.nan, "Book club", "Cycling", "Tennis Club", "Soccer Club", "Rowing",
                                       "Karate", "Baseball Club", "Comedy Club", "Feminism", "Dance Team",
                                       "Running", "Walking", "Cookies and Code", "Puppies Club", "Community Service",
                                       "Club 1", "Club 2", "Club 3", "Club 4", "Club 5", "Club 6", "Club 7",
                                       "Club 8", "Club 9", "Club 10", "Club 11", "Club 12", "Club 13", "Club 14",
                                       "Club 15", "Club 16", "Club 17"])
            #             "avg_rating": np.random.choice(
            #                 np.arange(0, 6, 1), p=[0.5, 0.05, 0.05, 0.30, 0.05, 0.05]
            #             ),
        }
        for x in range(num)
    ]
    return output
