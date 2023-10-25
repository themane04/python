print("Willkommen. Ich bin dein Taschenrechner. Welche Operation möchtest du durchführen?")
while True:
    print("""       
        1. Addition
        2. Subtraktion
        3. Multiplikation
        4. Division
        5. Taschenrechner beenden
                """)

    choice = int(input("Bitte gib die Nummer der gewünschten Operation ein: "))

    while choice < 1 or choice > 5:
        print("Ungültige Eingabe. Bitte versuche es erneut.")
        choice = int(input("Bitte gib die Nummer der gewünschten Operation ein: "))

    if choice in [1, 2, 3, 4]:
        num1 = float(input("Bitte gib die erste Zahl ein: "))
        num2 = float(input("Bitte gib die zweite Zahl ein: "))

        if choice == 1:
            print(f"Das Ergebnis: {num1 + num2}")
            print()
        elif choice == 2:
            print(f"Das Ergebnis: {num1 - num2}")
        elif choice == 3:
            print(f"Das Ergebnis: {num1 * num2}")
        elif choice == 4:
            if num2 == 0:
                print("Division durch Null ist nicht erlaubt!")
            else:
                print(f"Das Ergebnis: {num1 / num2}")
    elif choice == 5:
        print("Tschüss!")
        break
