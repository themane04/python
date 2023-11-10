def word_spinner():
    word = input("Please type in your word: ")
    words = word.split()
    list_of_words = []
    for word in words:
        reverse_word = word[::-1]
        if len(word) >= 5:
            list_of_words.append(reverse_word)
        else:
            list_of_words.append(word)

    final_sentence = " ".join(list_of_words)
    print("The fial sentence is: ", final_sentence)


word_spinner()
