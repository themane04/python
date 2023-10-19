"Aufgabe 1"
sum = 0
for i in range(1, 101):
    if i % 3 != 0 and i % 5 != 0:
        sum += i
print("Die Summe der Zahlen von 1 bis 100, die nicht durch 3, aber durch 5 teilbar sind, ist:", sum)