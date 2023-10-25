class Person:
    def __init__(self, pet):
        self.pets = [pet]

    def add_pet(self, pet):
        self.pets.append(pet)


person1 = Person("Lion")
person2 = Person("Snake")
person1.add_pet("Cat")
person1.pets.append("Dog")

print(person1.pets)
print(person2.pets)
