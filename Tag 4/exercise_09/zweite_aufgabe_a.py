class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


anm1 = Animal("Ben", 10)
anm2 = Animal("Ben2", 11)

print(anm1.__dict__, anm2.__dict__)
