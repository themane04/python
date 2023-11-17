import re


def is_creditcard_valid():
    user_input = input("Type in your credit card: ")
    valid_card_template = re.compile(r"^(?!.*(\d)\1\1\1)[4-6][0-9]{3}((-[0-9]{4}){3}|[0-9]{12})$")

    if valid_card_template.search(user_input):
        return True
    else:
        return False


func = is_creditcard_valid()
print(func)
