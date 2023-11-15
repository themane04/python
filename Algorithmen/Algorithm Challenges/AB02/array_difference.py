def get_valid_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That is not a number.")


first_list = []
second_list = []

print("\nFirst list")
for i in range(1, 6):
    first_list.append(get_valid_number(
        f"Type in the {i}{'st' if i == 1 else 'nd' if i == 2 else 'rd' if i == 3 else 'th'} NUMBER of the first list: "))

print("\nSecond list")
for i in range(1, 6):
    second_list.append(get_valid_number(
        f"Type in the {i}{'st' if i == 1 else 'nd' if i == 2 else 'rd' if i == 3 else 'th'} NUMBER of the second list: "))

set_of_the_second_list = set(second_list)
set_of_the_first_list = set(first_list)
result = set_of_the_first_list - set_of_the_second_list

print("\nThe first list is: ", first_list)
print("The second list is: ", second_list)
if not result:
    print("There are no unique elements in the first list that aren't in the second list.")
else:
    print("The unique elements in the first list that aren't in the second list are: ", result)
