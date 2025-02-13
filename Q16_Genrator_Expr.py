#Write a generator function that generates the first 10 even numbers.

Even_num = (i for i in range (2, 22, 2))

for j in Even_num:
    print(j)