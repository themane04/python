def calculate_pentagon_dots(n):
    if n <= 0:
        return False

    calculate_dots = ((5 * n * n) - (5 * n) + 2) / 2
    return calculate_dots


print(calculate_pentagon_dots(1))  # Iteration
