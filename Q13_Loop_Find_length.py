# Write a Python program to find the length of each string in List1.

List1 = ["Apple","Banana", "Cherry", "Date", "Elderberry"]

length = {i: len(i) for i in List1}

print(length)