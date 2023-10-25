# Aufgabe 3

""""
print("*")
print("**")
print("***")
print("****")
print("*****")
print("****")
print("***")
print("**")
print("*")
"""""

max_stars = 20
for i in range(1, max_stars + 1):
    print(i * "*")
for i in range(1, max_stars):
    print((max_stars - i) * "*")
