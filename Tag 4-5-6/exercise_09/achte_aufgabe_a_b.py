class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rarea(self):
        return self.length * self.width

    def sqarea(self):
        return self.length * 2


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


leng = float(input("Rectangle-Length: "))
wid = float(input("Rectangle-Width: "))

rec = Rectangle(length=leng, width=wid)
sq = Square(length=leng)
rec.rarea()
sq.sqarea()

print("Rectangle: ", rec.rarea())
print("Square: ", sq.sqarea())
