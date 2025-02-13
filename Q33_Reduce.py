#Write a Python program that uses reduce() to find the product of a list of numbers.

from functools import reduce

numbers = [2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)
print("Product of the list:", product)
