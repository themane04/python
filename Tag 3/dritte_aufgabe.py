def onetoten(n):
    if n == 0:
        return 0
    else:
        return n + onetoten(n - 1)


print(onetoten(10))
