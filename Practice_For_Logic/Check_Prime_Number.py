### USING A FUNCTION ###

from math import sqrt 

def isPrime(n): 
    if (n <= 1): 
        return False
    
    for i in range(2, int(sqrt(n))+1): 
        if (n % i == 0): 
            return False
        
    return True
  
  
num = int(input("Enter the number: "))
if isPrime(num): 
    print(f"{num} is a Prime Number") 
else: 
    print(f"{num} is not a Prime Number") 
  


### WITHOUT USING A FUNCTION ###

''' 

from math import sqrt

n = int(input("Enter a number to check: "))

if n <= 1:
    print(f"{n} is not a prime number.")
elif n <= 3:
    print(f"{n} is a prime number.")
else:
    # Assume the number is prime until proven otherwise
    is_prime = True
    
    # Check for factors from 2 up to the square root of n
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.") 

'''

'''
Why Iterate Up to the Square Root of n?

When checking if a number n is prime, we want to see if it has any divisors other than 1 and itself. 
If n has a divisor other than 1 and itself, it can be factored into two smaller numbers, a and b, such that:

n = a x b

If both a and b were greater than the square root of n, their product would be greater than n. 
Therefore, at least one of these factors must be less than or equal to the square root of n.

Example:
Let's say n is 36. The square root of 36 is 6. The pairs of factors of 36 are:

1 x 36
2 x 18
3 x 12
4 x 9
6 x 6

Notice that all pairs involve at least one number that is less than or equal to 6 (the square root of 36).

Efficiency:
By only checking for factors up to the square root of n, we reduce the number of iterations significantly, especially for large numbers. 
This makes our primality test more efficient.

Adding 1:
In the code, we use int(math.sqrt(n)) + 1 to include the integer part of the square root of n in our range. 
This ensures we don't miss any potential factors that are exactly equal to the square root.

'''