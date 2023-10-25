def double(b):
    return b * 2


a = float(input("Number: "))

while a < 100:
    a = double(a)
    print("Doubled number:", a)
