#Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue statement. List1

List1 = ['apple', 'banana', 'mango']
print(List1,"\n")

for i in List1:
    if i == 'banana':
        continue
    print(i)