def clear_screen():
    print("\n" * 50)


correct_guesses = []
incorrect_guesses = []
player1 = input("Player one is: ")
player2 = input("Player two is: ")

while player1 == player2:
    print("Both players can not have the same name dumbass!")
    player2 = input("Player two is: ")
else:
    pass

guess_word = input(f"{player1} type in the word: ").upper()
clear_screen()
number_of_incorrect_guesses = int(input(f"How many incorrect guesses is {player2} allowed to: "))
score = number_of_incorrect_guesses
player_names = [player1, player2]
show_word = "_" * len(guess_word)

while len(incorrect_guesses) < number_of_incorrect_guesses:
    letter_guess = input("Type in a letter: ").upper()

    if "_" not in show_word or letter_guess == guess_word:
        print(f"Congratualations. {player2} has won!")
        break

    elif letter_guess not in guess_word:
        score -= 1
        print("Guesses left: ", score)
    else:
        print("Guesses left: ", score)

    display_word_list = list(show_word)
    if letter_guess in guess_word:
        correct_guesses.append(letter_guess)
    else:
        incorrect_guesses.append(letter_guess)

    for index, character in enumerate(guess_word):
        if character == letter_guess:
            display_word_list[index] = letter_guess

    show_word = "".join(display_word_list)
    print(show_word)
if "_" in show_word:
    print(f"Nice Try! {player1} has won!")
