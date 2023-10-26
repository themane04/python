class Rectangle:
    def __init__(self, leng, wid, hei):
        self.length = leng
        self.width = wid
        self.height = hei

    def area(self):
        return self.length * self.width

    def volume(self):
        return self.length * self.width * self.height


height = float(input("Type in the height: "))
length = float(input("Type in the length: "))
width = float(input("Type in the width: "))

vol = Rectangle(leng=length, wid=width, hei=height)
res = Rectangle(leng=length, wid=width, hei=height)

print(f"The area is: {res.area()}")
print(f"The voulme is: {res.volume()}")
