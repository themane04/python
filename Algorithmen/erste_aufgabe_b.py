import random


def create_random_array(size=10):  # I can change the size of the array here
    return [random.randint(1, 100) for i in range(size)]


random_array = create_random_array()

print(random_array)
