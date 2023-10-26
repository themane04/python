class Person:
    pets = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def addpet(self, pet):
        self.pets.append(pet)


person1 = Person("Ben10", 12)
person1.addpet("Bear")
person1.addpet("Giraffe")
person1.addpet("Elephant")
person1.addpet("Lion")
person1.addpet("Tiger")

print("Ben10 hat die folgenden Tiere:", Person.pets)
