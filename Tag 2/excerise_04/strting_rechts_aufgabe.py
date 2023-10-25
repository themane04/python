me = input("String: ")
new_str = ""

for element in me:
    if element == ' ':
        new_str += ' '
    else:
        shifted = chr(((ord(element.lower()) - ord('a') + 2) % 26) + ord('a'))

        if element.isupper():
            new_str += shifted.upper()
        else:
            new_str += shifted.lower()

print("Verschobener String:", new_str)
