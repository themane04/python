def fun(*args):
    res = sum(args[1:])
    fnum = args[0]
    return res * fnum


result = fun(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)


def word(*argv):
    for arg in argv:
        print(arg)
        

word("Hallo", "Ich bin Ben", "Ich bin du..schlau")
