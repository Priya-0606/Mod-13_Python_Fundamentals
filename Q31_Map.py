#Write a Python program to apply the map() function to square a list of numbers.

def square(n):
    return n*n
number = [1, 3, 5, 9, 8, 2, 7]
result = map(square, number)
print(list(result))

