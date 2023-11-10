def get_height():
    height = float(input("Type in the height: "))
    bounce = float(input("Type in the bounce: "))
    window = float(input("Type in the distance from the window: "))
    sights = 0

    if height > 0 and 0 < bounce < 1 and window < height:
        sights = 1
        height *= bounce

        while height > window:
            sights += 2
            height *= bounce

    return sights if sights > 0 else -1


result = get_height()
print("The result is:", result)
