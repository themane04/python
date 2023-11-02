import random

user_input = int(input("Type in the length for your numbers up until 42: "))

numlist = list(range(1, 43))
res = list()

print("""
    Do you have some numbers that you want in the list?
    1. Yes
    2. No
    """)

user_input2 = int(input("Choice: "))

if user_input2 == 1:
    usernum = int(input("How many do you want to add?: "))
    for i in range(usernum):
        manual_number_from_user = int(input("Enter a number between 1 and 42: "))
        if manual_number_from_user in numlist:
            res.append(manual_number_from_user)
            numlist.remove(manual_number_from_user)
        else:
            pass

    remaining_count = user_input - len(res)

    for i in range(remaining_count):
        randomind = random.choice(numlist)
        res.append(randomind)
        numlist.remove(randomind)

    if user_input > 42 or user_input < len(res):
        print("Invalid total count.")

if user_input2 == 2:
    if user_input > 42:
        print("That is more than 42.")
    else:
        for i in range(user_input):
            randomind = random.choice(numlist)
            res.append(randomind)
            numlist.remove(randomind)

print("Numbers: ", res)
lucky_num = random.choice(res)
print("Lucky Number: ", lucky_num)
