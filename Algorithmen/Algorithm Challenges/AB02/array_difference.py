first_list = []
print("")
print("First list")
element1_first_list = int(input("Type in the 1st NUMBER of the first list: "))
element2_first_list = int(input("Type in the 2nd NUMBER of the first list: "))
element3_first_list = int(input("Type in the 3rd NUMBER of the first list: "))
element4_first_list = int(input("Type in the 4th NUMBER of the first list: "))
element5_first_list = int(input("Type in the 5th NUMBER of the first list: "))

print("")
print("Second list")
first_list.append(element1_first_list)
first_list.append(element2_first_list)
first_list.append(element3_first_list)
first_list.append(element4_first_list)
first_list.append(element5_first_list)

second_list = []
element1_second_list = int(input("Type in the 1st NUMBER of the second list: "))
element2_second_list = int(input("Type in the 2nd NUMBER of the second list: "))
element3_second_list = int(input("Type in the 3rd NUMBER of the second list: "))
element4_second_list = int(input("Type in the 4th NUMBER of the second list: "))
element5_second_list = int(input("Type in the 5th NUMBER of the second list: "))

second_list.append(element1_second_list)
second_list.append(element2_second_list)
second_list.append(element3_second_list)
second_list.append(element4_second_list)
second_list.append(element5_second_list)

set_of_the_second_list = set(second_list)
set_of_the_first_list = set(first_list)
result = set_of_the_first_list - set_of_the_second_list


print("The first list is: ", first_list)
print("The second list is: ", second_list)
if not result:
    print("There are no unique elements in the first list that aren't in the second list.")
else:
    print("The unique elements in the first list that aren't in the second list are: ", result)
