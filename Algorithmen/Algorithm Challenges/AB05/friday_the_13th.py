import calendar


def has_friday_13(month, year):
    date = calendar.weekday(year, month, 13)

    if date == calendar.FRIDAY:
        return True
    else:
        return False


friday_checker = has_friday_13(3, 2020)
print(friday_checker)
