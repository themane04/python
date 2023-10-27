class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello {self.name}!")
        print(f"You {self.name} are {self.age} years old!")


nam = input("Name: ")
ag = input("Age: ")

output = Person(name=nam, age=ag)

output.introduce()
