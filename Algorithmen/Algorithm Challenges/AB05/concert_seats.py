def check_vision(seat_rows):
    for i in range(1, len(seat_rows)):
        for j in range(0, len(seat_rows[i])):
            if j >= len(seat_rows[i - 1]):
                continue
            if seat_rows[i][j] <= seat_rows[i - 1][j]:
                return False
    return True


seats_east = [[1, 2, 3, 2, 1, 1],
              [2, 4, 4, 3, 2, 2],
              [5, 5, 5, 5, 4, 4],
              [6, 6, 7, 6, 5, 5]]

seats_west = [[4, 1, 2, 4, 4],
              [5, 4, 6, 4, 2],
              [1, 5, 3, 2, 2],
              [6, 4, 5, 5, 6],
              [3, 2, 3, 3, 1]]

seats_north = [[1, 2, 1, 7, 6, 6],
               [3, 7, 4, 1, 4, 4],
               [4, 7, 3, 2, 4, 3],
               [6, 2, 3, 6, 1, 7]]

seats_south = [[1, 1, 1, 1, 1, 1, 1],  # first row
               [2, 2, 2, 2, 2, 2, 2],  # second row
               [3, 3, 3, 3, 3, 3, 3]]  # third row

vision = check_vision(seats_east), check_vision(seats_west), check_vision(seats_north), check_vision(seats_south)
print(vision)
