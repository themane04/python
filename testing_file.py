def thousands_separator(num: int) -> str:
    string = str(num)
    for i in range(len(string) - 3, 0, -3):
        string = string[:i] + "'" + string[i:]

    return string


func = thousands_separator(1000000000000)
print(func)
