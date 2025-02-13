#Write a Python program that uses a custom iterator to iterate over a list of integers.

def integer_iterator(numbers):
    for num in numbers:
        yield num  # Yield each number one by one

# List of integers
numbers = [10, 20, 30, 40, 50]

# Using the generator as an iterator
iterator = integer_iterator(numbers)

# Iterate using a for loop
for num in iterator:
    print(num)
