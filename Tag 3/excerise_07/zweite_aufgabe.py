def mylist(element):
    res = 0
    for i in element:
        res += i
    print("The result is: ", res)
    return


elements = [i for i in range(16)]
print(elements)

mylist(elements)
