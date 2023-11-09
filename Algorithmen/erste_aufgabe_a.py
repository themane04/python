import random
import string


def number_array(size=100, min_value=1, max_value=100):
    return [random.randint(min_value, max_value) for _ in range(size)]


def letter_array(size=50):
    return [random.choice(string.ascii_letters) for _ in range(size)]


numbers = number_array()
letters = letter_array()

print(numbers)
print(letters)
