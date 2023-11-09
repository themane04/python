n = int(input("Type in the number: "))


def factorial_number():
    fact1 = 1
    for i in range(1, n + 1):
        fact1 = fact1 * i
    return fact1


print(factorial_number())
