print("Time converter from a whole number!")


def human_readable_time():
    number_from_user = int(input("Type in your positive whole number: "))

    while number_from_user < 0 or number_from_user > 359999:
        print("The number you typed in is either negative or bigger than 359999.")
        number_from_user = int(input("Type in your positive whole number: "))
    else:
        total_hours = int(number_from_user / 3600)
        remaining_seconds = number_from_user % 3600
        total_minutes = int(remaining_seconds / 60)
        total_seconds = int(remaining_seconds % 60)
        print(f"{int(total_hours):02d}h:{int(total_minutes):02d}min:{int(total_seconds):02d}s")


human_readable_time()
