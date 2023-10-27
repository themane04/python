class Rectangle:
    def __init__(self, leng, wid):
        self.length = leng
        self.width = wid

    def area(self):
        return self.length * self.width


length = float(input("Type in the length: "))
width = float(input("Type in the width: "))

res = Rectangle(leng=length, wid=width)

print(f"The result is {res.area()}")
