from Algorithmen.zweite_aufgabe_b import myarray
import time


def insertion_sort(array):
    n = len(array)
    if n <= 1:
        return

    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            j -= 1
        array[j + 1] = key


my_array = myarray(100000)  # How many numbers
times = []

for _ in range(100):
    new_array = []
    start_time = time.time()
    insertion_sort(my_array)
    end_time = time.time()
    times.append(end_time - start_time)
average_time = sum(times) / len(times)

print("The time is: ", times)
print("The average time is: ", average_time)
