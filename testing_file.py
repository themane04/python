def change(numbers: list):
    numbers.append(30)


my_numbers = [10, 20]

print('Vor der Funktion: ', my_numbers)

change(my_numbers)

print('Nach der Funktion: ', my_numbers)