class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name, "Wuff")


dog1 = Dog("Bello", 5)
dog1.bark()
