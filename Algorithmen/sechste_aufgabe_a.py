def merge_sort(array):
    # Base case: if the array is of length 1 or less, it's already sorted
    if len(array) > 1:
        # Find the middle of the array
        mid = len(array) // 2
        # Split the array into two halves
        L = array[:mid]  # Left half
        R = array[mid:]  # Right half

        # Recursively sort each half
        merge_sort(L)
        merge_sort(R)

        # Initialize pointers for L(left array), R(right array), and array(merged array)
        i = j = k = 0

        # Merge the two halves
        while i < len(L) and j < len(R):
            # Compare elements from each half and put the smaller one in the array
            if L[i] < R[j]:
                array[k] = L[i]  # Take from left
                i += 1
            else:
                array[k] = R[j]  # Take from right
                j += 1
            k += 1

        # If any elements are left in L, add them to the array
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        # If any element are left in R, add them to the array
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1


# Example
myarray = [5, 10, 20, 50, 2222, 49, 1.2, 59]
merge_sort(myarray)
print("Sorted array is: ", myarray)
