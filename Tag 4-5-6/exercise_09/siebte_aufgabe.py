class Person:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def world():
        print("Hello World!")

    def get_name(self):
        return self.name

    def add_str_with_value(cls, attribute, value):
        setattr(cls, attribute, value)


person1 = Person("John")
person1.world()
print(person1.name)
person1.add_str_with_value("age", 14)
print(person1.age)
