person = {
    "firstname":"Max",
    "lastname":"Mustermann",
    "age":"42",
    "married":True,
    "kids": [
        {
            "firstname":"Larissa",
            "age": 12
        },
        {
            "firstname": "Dominic",
            "age": 12
        }
    ]
}

print(person["kids"][0]["firstname"])
print(person["kids"][1]["age"])