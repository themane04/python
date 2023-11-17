def add_thousands_seperator(num):
    if num <= 0:
        return False

    number_string = str(num)

    final_result = ""
    counter = 0

    for character in reversed(number_string):
        final_result += character
        counter += 1
        if counter % 3 == 0 and counter != 0:
            final_result += "'"

    final_result = "".join((reversed(final_result)))
    return final_result


seperator = add_thousands_seperator(34593458206)
print(seperator)
