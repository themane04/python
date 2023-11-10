def multiply():
    number_from_user = int(input("Type in your number: "))

    if number_from_user < 0:
        print(0)
    else:
        sum_of_the_numbers = 0
        for number in range(1, number_from_user):
            if number % 5 == 0 or number % 3 == 0:
                sum_of_the_numbers += number
        print("The sum of the numbers:", sum_of_the_numbers)


multiply()
