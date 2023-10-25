fruits = ["orange", "apple", "pear", "banana", "kiwi", "banana", "apple", "banana"]

fruits.append("orange")

print("Vor dem Entfernen: ", fruits)


def new_list(fruit, element):
    while element in fruit:
        fruit.remove(element)


new_list(fruits, "banana")

print("Nach dem Entfernen: ", fruits)
