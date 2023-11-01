import abc
from abc import ABC


class Animal(abc.ABC):
    def __init__(self, milk_production, egg_production, meat_production, call):
        self.call = call
        self.milk_production = milk_production
        self.egg_production = egg_production
        self.meat_production = meat_production

    @abc.abstractmethod
    def make_call(self):
        pass


class Cow(Animal, ABC):
    def __init__(self, milk_production):
        super().__init__(milk_production)


class Chicken(Animal, ABC):
    def __init__(self, egg_production):
        super().__init__(egg_production)


class Pig(Animal, ABC):
    def __init__(self, meat_production):
        super().__init__(meat_production)


"""
steps:

Step 1: Create the Animal Abstract Class
1.1 Create an abstract class called Animal.
1.2 Add an attribute called call.
1.3 Define an abstract method make_call().

Step 2: Implement the Specific Animals
2.1 Create classes for at least 3 animals, e.g., Cat, Dog, Cow.
2.2 Inherit these classes from the Animal abstract class.
2.3 Implement a unique attribute for each animal. For example, milk_production for Cow.
2.4 Implement a unique method for each animal. For example, produce_milk() for Cow.

Step 3: Create the Farm Class
3.1 Create a class called Farm.
3.2 Add an attribute called Animals, which will be a list holding all the animal objects.
3.3 Create a method called animal_list() that will print the list of animals on the farm.
3.4 Create a method called summary() to show the count of each type of animal in a dictionary format.
3.5 Create a method to add an animal object to the Animals list.

Step 4: Test the Farm
4.1 Create instances of each animal.
4.2 Use the Farm class's method to add these instances to the Animals list.
4.3 Use the animal_list() and summary() methods to display the animals and their counts.

Step 5: Additional Functionality (Optional)
5.1 Implement any additional functionality or attributes you find interesting or relevant.
"""