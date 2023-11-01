import os

print(os.pardir)

with open("demo1.txt", "w") as f:
    f.write("Zeile1")
    f.write("\nZeile2")
    f.write("\nZeile3")
