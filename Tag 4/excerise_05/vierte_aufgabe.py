import random

lst = []

for i in range(5):
    under_lst = []
    for j in range(5):
        randomnum = random.randint(1, 5)
        under_lst.append(randomnum)
    lst.append(under_lst)

print(lst)
