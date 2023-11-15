class RomanNumerals:
    def to_roman_number(self):
        user_input = int(input("Type in the year with normal numbers: "))

        result = str()
        while user_input > 0:
            if user_input - 1000 >= 0:
                result += "M"
                user_input -= 1000
            elif user_input - 900 >= 0:
                result += "CM"
                user_input -= 900
            elif user_input - 500 >= 0:
                result += "D"
                user_input -= 500
            elif user_input - 400 >= 0:
                result += "CD"
                user_input -= 400
            elif user_input - 100 >= 0:
                result += "C"
                user_input -= 100
            elif user_input - 90 >= 0:
                result += "XC"
                user_input -= 90
            elif user_input - 50 >= 0:
                result += "L"
                user_input -= 50
            elif user_input - 40 >= 0:
                result += "XL"
                user_input -= 40
            elif user_input - 10 >= 0:
                result += "X"
                user_input -= 10
            elif user_input - 9 >= 0:
                result += "IX"
                user_input -= 9
            elif user_input - 5 >= 0:
                result += "V"
                user_input -= 5
            elif user_input - 4 >= 0:
                result += "IV"
                user_input -= 4
            else:
                result += "I"
                user_input -= 1
        print("The year with roman numbers: ", result)

    def from_roman_number(self):
        user_input = input("Type in the year with roman numbers: ")
        roman_symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0

        i = 0
        while i < len(user_input):
            # Durchlaufen der Eingabezeichenkette 'user_input', Zeichen für Zeichen.

            current_symbol = user_input[i]
            # Zugriff auf das aktuelle Zeichen an Position 'i' in der Eingabe.

            current = roman_symbols[current_symbol]
            # Umwandlung des aktuellen römischen Symbols in seinen numerischen Wert.

            if i + 1 < len(user_input):
                # Überprüfen, ob es ein nächstes Zeichen in 'user_input' gibt.

                next_symbol = user_input[i + 1]
                # Zugriff auf das nächste Zeichen nach dem aktuellen Zeichen.

                next_ = roman_symbols[next_symbol]
                # Umwandlung des nächsten römischen Symbols in seinen numerischen Wert.

                if current < next_:
                    # Wenn der Wert des aktuellen Symbols kleiner ist als der des nächsten Symbols,
                    # dann subtrahieren Sie den aktuellen Wert von 'result'.
                    result -= current
                else:
                    # Wenn der Wert des aktuellen Symbols nicht kleiner als der des nächsten Symbols ist,
                    # dann addieren Sie den aktuellen Wert zu 'result'.
                    result += current
            else:
                # Wenn es kein nächstes Zeichen gibt (d.h. das aktuelle Zeichen ist das letzte Zeichen),
                # dann addieren Sie einfach den Wert des aktuellen Symbols zu 'result'.
                result += current

            i += 1
            # Erhöhung des Index 'i', um zum nächsten Zeichen in der Eingabe überzugehen.

        print("The year with normal numbers: ", result)


while True:
    try:
        print("""
        Choose what do you want to do.
            1. From normal to roman
            2. From roman to normal
        """)

        roman = RomanNumerals()
        user_choice = int(input("Your choice: "))
        if user_choice == 1:
            roman.to_roman_number()
        elif user_choice == 2:
            roman.from_roman_number()
        else:
            print("Please choose either 1 or 2.")
    except ValueError:
        print("That an invalid choice. Please choose either 1 or 2.")
