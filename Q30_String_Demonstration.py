#Write a Python program that manipulates and prints strings using various string methods.

Str = "  Hello, Python Programming!  "

Original_String = Str.strip()
print("Stripped Text:", Original_String)

print("Uppercase:", Original_String.upper())
print("Lowercase:", Original_String.lower())

new_str = Original_String.replace("Python", "Java")
print("Replaced Text:", new_str)

words = Original_String.split()
print("Split Words:", words)

position = Original_String.find("Python")
print("Position of 'Python':", position)

print("Starts with 'Hello':", Original_String.startswith("Hello"))
print("Ends with 'Programming!':", Original_String.endswith("Programming!"))

count = Original_String.count("o")
print("Count of 'o':", count)

joined_str = "-".join(words)
print("Joined Text:", joined_str)

print("Title Case:", Original_String.title())

reversed_str = Original_String[::-1]
print("Reversed Text:", reversed_str)
