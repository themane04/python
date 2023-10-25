def prob(x):
    step = 0
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
            step += 1
    return step


num = int(input("Your number: "))
steps = prob(num)
print(f"The total steps: {steps}")
