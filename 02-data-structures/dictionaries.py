# Dictionaries (key-value pairs)

person = {
    "name": "Christoffer",
    "age": 20,
    "student": True
}

print(person["name"])
print(person["age"])

# Add new key
person["city"] = "Bergen"

# Update value
person["age"] = 21

for key, value in person.items():
    print(key, ":", value)
