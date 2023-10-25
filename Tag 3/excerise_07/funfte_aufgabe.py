def calc_root(num, m=2):
    res = num ** (1 / m)
    res = round(res, 2)
    return res


print(calc_root(1000, 3))
