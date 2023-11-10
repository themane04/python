def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    north_south_position = 0
    east_west_position = 0

    for step in walk:
        if step == "n":
            north_south_position += 1
        elif step == "s":
            north_south_position -= 1
        elif step == "e":
            east_west_position += 1
        else:
            east_west_position -= 1
    if north_south_position == 0 and east_west_position == 0:
        return True
    else:
        return False


first_walk = ["n", "s", "n", "s", "n", "s", "n", "s", "n"]
result = is_valid_walk(walk=first_walk)
print("Is the walk correct: ", result)
