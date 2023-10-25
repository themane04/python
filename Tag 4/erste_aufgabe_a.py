fruits = ["orange", "apple", "pear", "banana", "kiwi", "banana", "apple", "banana"]

banana = fruits.count("banana")

fruits.append("orange")

fruits.insert(1, "kiwi")

fruits.pop(1)

fruits.pop(3)
fruits.pop(5)
fruits.pop(7)

print(fruits)
print("Banana kommt", banana, "mal vor")
