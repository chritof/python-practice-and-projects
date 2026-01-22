# Dictionaries

person = {
    "name": "Christoffer",
    "age": 20,
    "student": True
}

print(person["name"])
print(person["age"])

person["age"] = 21

for key, value in person.items():
    print(key, ":", value)
