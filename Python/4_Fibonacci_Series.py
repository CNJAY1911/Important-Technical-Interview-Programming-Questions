# Defining function to implement Logic for printing Fibonnaci Series

def fibonacci_series(n):
    a = 0
    b = 1
    print(a, b, end = " ")
    for i in range(2, n):
        c = a + b
        print(c, end = " ")
        a = b
        b = c

n = int(input("Enter number of terms: "))
fibonacci_series(n)