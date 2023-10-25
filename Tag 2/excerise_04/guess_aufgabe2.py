import random

pnumber = random.randint(1, 100)

user = 0

while user != pnumber:
    user = int(input("Guess: "))

    if user == pnumber:
        print("You guessed the number!")
        break
    elif user < pnumber:
        print("The number is bigger!")
    elif user > pnumber:
        print("The number is smaller!")
