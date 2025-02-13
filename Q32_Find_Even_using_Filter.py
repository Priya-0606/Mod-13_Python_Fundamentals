# Write a Python program that filters out even numbers using the filter() function.

def is_even(n):
    return n % 2 == 0 

number = [13,25,35,46,56,68,79,96]

result = list(filter(is_even, number))

print(result) 