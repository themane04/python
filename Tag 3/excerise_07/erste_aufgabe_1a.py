# Aufgabe 1a
from datetime import datetime


def now():
    dnow = datetime.now()
    current_time = dnow.strftime("%H:%M:%S")
    print("Current time:", current_time)


now()
now()
