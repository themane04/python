def clear_screen():
    print("\n" * 50)


correct_guesses = []
incorrect_guesses = []
print("Player one needs to type in the word and player two has to guess it!")
player1 = input("Player one is: ")
player2 = input("Player two is: ")

while player1 == player2:
    print("Both players can't have the same name dumbass!")
    player1 = input("Player one is: ")
    player2 = input("Player two is: ")
else:
    pass

guess_word = input(f"{player1} type in the word: ").upper()
clear_screen()
number_of_incorrect_guesses = int(input(f"How many incorrect guesses is {player2} allowed to: "))
score = number_of_incorrect_guesses
player_names = [player1, player2]
show_word = ''.join(['_' if letter != ' ' else ' ' for letter in guess_word])
show_word_list = list(show_word)

while len(incorrect_guesses) < number_of_incorrect_guesses:
    print(show_word)
    letter_guesses = input("Type in a letter or letters: ").upper()
    changes_made = False

    for letter_guess in letter_guesses:
        if letter_guess in guess_word and letter_guess not in correct_guesses:
            for index, character in enumerate(guess_word):
                if character == letter_guess:
                    show_word_list[index] = letter_guess
            correct_guesses.append(letter_guess)
            changes_made = True
        elif letter_guess not in guess_word and letter_guess not in incorrect_guesses:
            incorrect_guesses.append(letter_guess)
            score -= 1
            changes_made = True

    if not changes_made:
        print("No new correct or incorrect letters guessed.")

    show_word = "".join(show_word_list)
    print(show_word)
    print("Guesses left: ", score)

    if "_" not in show_word:
        print(f"Congratulations. {player2} has won! The word was: ", "'", guess_word, "'")
        break

if "_" in show_word.replace(' ', ''):
    print(f"Nice Try! {player1} has won!")
    print(f"The word was: ", "'", guess_word, "'")
