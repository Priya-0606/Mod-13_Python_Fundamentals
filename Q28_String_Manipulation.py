#Write a Python program to demonstrate string slicing.

S = "Tops Technologies"
print("Original String: ", S)
print("Sliced String: ", S[0:5])  # Slicing from index
print("Sliced String: ", S[0:5:1]) 
print("Sliced String: ", S[0:5:2])  
print("Reverse : ", S[::-1])
print("Alternate Character : ", S[::2])
print("Sub String : ", S[1:11:])
print("SubString : ", S[4:11:])
print("Sub String : ", S[11:14:])
print("Sub String : ", S[11::])
