class Person:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def world():
        print("Hello World!")

    @staticmethod
    def addel(self, key, value):
        self.key = value

    def get_name(self):
        return self.name


person1 = Person("John")
person1.world()
print(person1.name)
print(Person.world())
person1.addel("name", "thomas")
