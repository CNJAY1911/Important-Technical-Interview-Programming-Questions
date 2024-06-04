# Logic for checking and getting prime numbers
# in a given range using 2 functions

from math import sqrt 

def isPrime(n): 
    if (n <= 1): 
        return False
    
    for i in range(2, int(sqrt(n))+1): 
        if (n % i == 0): 
            return False
        
    return True

def printPrime(a,b):
    for i in range(a,b+1):
        if(isPrime(i)):
            print(i, end = " ")

a,b = map(int, input("Enter the range: ").split(" "))
printPrime(a,b)
