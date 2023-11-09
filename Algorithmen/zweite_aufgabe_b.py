import random
import time


def myarray(size=100):
    return [random.randint(1, 1000000) for i in range(size)]


start = time.time()
my_array = myarray()

print(my_array)

end = time.time()
print(end - start)
