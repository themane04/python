import re

email = input("Type in the E-Mail: ")

regex_code = r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})"

match = re.search(regex_code, email)

if match is None:
    print("Email was invalid")
else:
    print("Local Part:          ", match.group(1))
    print("Second Level Domain: ", match.group(2))
    print("Main Domain:         ", match.group(3))
