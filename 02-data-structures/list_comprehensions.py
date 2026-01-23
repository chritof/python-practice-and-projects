# List comprehensions

numbers = [1, 2, 3, 4, 5]

squared = [n * n for n in numbers]
even_numbers = [n for n in numbers if n % 2 == 0]

print("Squared:", squared)
print("Even numbers:", even_numbers)
