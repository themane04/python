def calculate_height_of_pyramide(ball):
    level = -1
    ball_in_level = 0

    while ball >= ball_in_level:
        ball = ball - ball_in_level
        level += 1
        ball_in_level += 1
    return level


number_from_user = int(input("Type in your number: "))
result = calculate_height_of_pyramide(ball=number_from_user)
print("The height of the pyramide is: ", result)
