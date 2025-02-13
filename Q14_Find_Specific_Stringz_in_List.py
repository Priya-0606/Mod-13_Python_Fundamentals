#Write a Python program to find a specific string in the list using a simple 
#for loop and if condition.

L1 = ["Apple","Banana", "Cherry", "Date", "Elderberry"]
target = "Cherry"

S = False
for i in L1:
    if i == target:
        S = True
        break

if S:
    print(target, "is found in the list")
else:
    print(target, "is not found in the list")