from math import sqrt

n = int(input("Enter a number to check: "))

if n <= 1:
    print("Not a Prime Number.")
elif n <= 3:
    print("Prime Number.")
else:
    # Assume the number is prime until proven otherwise
    is_prime = True
    
    # Check for factors from 2 up to the square root of n
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("Prime Number.")
    else:
        print("Not a Prime Number.") 