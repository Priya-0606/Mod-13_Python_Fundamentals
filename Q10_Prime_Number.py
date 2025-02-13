A = int(input("Enter a number: "))

if A > 1:
    for i in range(2, int(A**0.5) + 1):  # Check up to square root of A
        if (A % i) == 0:
            print(A, "is not a prime number")
            break
    else:  
        print(A, "is a prime number")
else:
    print(A, "is not a prime number")  