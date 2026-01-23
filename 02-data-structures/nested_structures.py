# Nested data structures

students = [
    {"name": "Anna", "age": 21},
    {"name": "Ola", "age": 22},
    {"name": "Christoffer", "age": 20}
]

for student in students:
    print(student["name"], "is", student["age"], "years old")
