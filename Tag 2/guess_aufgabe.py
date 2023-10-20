import random
pnumber = random.randint(1,10)

user = 0

while user != pnumber:
    user = int(input("Guess: "))

    if user == pnumber:
        print("You guessed the number!")
        break
    else:
        print("You missed! Try again!")
