import re


def is_creditcard_valid():
    user_input = input("Type in your credit card: ")
    valid_card_template = re.compile(r"^(?!(\d)(\1{3}))[456](?=(?:\d{4}-){3}\d{4}$|\d{16}$)(?:\d{4}-?){3}\d{4}$")

    if valid_card_template.match(user_input):
        return True
    else:
        return False


func = is_creditcard_valid()
print(func)
