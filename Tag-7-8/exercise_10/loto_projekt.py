import random

while True:
    # Ask for how many numbers the user wants (max 42)
    while True:
        try:
            user_input = int(input("How many numbers do you want to draw? (1–42): "))
            if 1 <= user_input <= 42:
                break
            else:
                print("Please enter a number between 1 and 42.")
        except ValueError:
            print("That wasn't a number, try again.")

    numlist = list(range(1, 43))
    res = []

    # Ask if the user wants to add specific numbers
    print("""
Do you want to pick some of your own numbers?
1. Yes
2. No
""")

    while True:
        try:
            user_input2 = int(input("Choice (1 or 2): "))
            if user_input2 in [1, 2]:
                break
            else:
                print("Pick 1 or 2.")
        except ValueError:
            print("Enter a number, not text 😅")

    if user_input2 == 1:
        while True:
            try:
                usernum = int(input("How many numbers do you want to pick manually?: "))
                if 0 <= usernum <= user_input:
                    break
                else:
                    print(f"You can only pick up to {user_input} numbers.")
            except ValueError:
                print("Just a number please.")

        for i in range(usernum):
            while True:
                try:
                    manual_number = int(input(f"Enter number {i + 1} (1–42): "))
                    if 1 <= manual_number <= 42 and manual_number in numlist:
                        res.append(manual_number)
                        numlist.remove(manual_number)
                        break
                    else:
                        print("Invalid or duplicate number. Try again.")
                except ValueError:
                    print("Invalid input.")

    # Fill remaining numbers randomly
    remaining_count = user_input - len(res)
    res += random.sample(numlist, remaining_count)

    # Final output
    print("🎉 Your lottery numbers:", sorted(res))
    print("🍀 Your lucky number is:", random.choice(res))

    # Ask if the user wants to play again
    again = input("\nWanna try your luck again? (y/n): ").strip().lower()
    if again != 'y':
        print("Thanks for playing! 🎲")
        break
