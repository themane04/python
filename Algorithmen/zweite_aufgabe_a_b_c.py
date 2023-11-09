import time

from Algorithmen.zweite_aufgabe_b import myarray


def sorting_bubble(array):
    n = len(array)
    swapped = False
    for i in range(n - 1):  # The outer loop goes from 0 up until "n-1"
        for j in range(0, n - i - 1):  # The inner loop goes from 0 to "n-i-1"
            if array[j] > array[j + 1]:  # Chack in the inner loop if the element is bigger than
                # the element on the right side of it
                swapped = True  # When the elements are in the wrong order and when they need to be changed
                array[j], array[j + 1] = array[j + 1], array[j]  # The elements will be changed when the left element
                # is bigger than the right one
        if not swapped:  # Check if there was a change
            return


times = []
myarray1 = myarray(10000)  # The number of elements that have to be sorted

for _ in range(100):
    new_array = []
    start_time = time.time()
    sorting_bubble(myarray1)
    end_time = time.time()
    times.append(end_time - start_time)
average_time = sum(times) / len(times)

print("The time is: ", times)
print("The average time is: ", average_time)
# It needs double more time
