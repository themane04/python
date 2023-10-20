def prob(x):
    steps = 0
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
            steps += 1
    return steps

num = int(input("Your number: "))
steps = prob(num)
print(f"The total steps: {steps}")
