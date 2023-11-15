company_name = input("Type in the name of the company: ")

letter_list = {}

for letter in company_name:
    if letter not in letter_list:
        letter_list[letter] = 1
    else:
        letter_list[letter] += 1

converted_list = []
for letter, count in letter_list.items():
    converted_list.append([letter, count])

    # Sorts the list 'converted_list' in descending order based on the count of each letter.
    # 'key=lambda x: x[1]' tells Python to use the second element of each sublist (the count) for sorting.
    # This will first sort the elements by the count in descending order (due to the negative sign in -x[1]) and then
    # alphabetically by the letter (using x[0]) for ties in the count.
    converted_list.sort(key=lambda x: (-x[1], x[0]))

print(converted_list)
