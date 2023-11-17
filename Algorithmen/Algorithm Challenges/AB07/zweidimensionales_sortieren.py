def two_dimensional_sort(array):
    for i, row in enumerate(array):
        if len(row) != len(array):
            you_are_a_faliure = i + 1
            raise Exception(f"Row length does not match the array's first dimension. First error at", you_are_a_faliure,
                            "row")

    list_for_all_elements = []
    for row in array:
        for element in row:
            list_for_all_elements.append(element)

    flattened_list = sorted(list_for_all_elements)
    final_two_dimensional_array = []
    row_length = len(array[0])

    for i in range(0, len(flattened_list), row_length):
        row = flattened_list[i:i + row_length]
        final_two_dimensional_array.append(row)

    return final_two_dimensional_array


first_list = [
    [2, 8, 9, 6],
    [4, 7, 3, 10],
    [14, 5, 12, 1],
    [13, 15, 16, 11]
]

second_list = [
    [1, 2, 3, 4],
    [5, 6, 7],
    [8, 9, 10],
    [11, 12, 13]
]

first_array_sorter = two_dimensional_sort(first_list)
# second_array_sorter = two_dimensional_sort(second_list)  # the problmeatic one
print(first_array_sorter)
