'''
Arun is a bus conductor. His tickets machine is printing numbers in 
reverse order due to a technical glitch. As a programmer on the bus,
you are asked to help him by creating a program to display the numbers correctly.

Example:
Input: 320
Output: Number in reverse order -> 23

Input: 231
Output: Number in reverse order -> 132
'''

# Logic for Reversing a Number

num = int(input("Enter the number: "))
result = 0

while num > 0:
    digit = num % 10
    result = (result * 10) + digit
    num = num // 10

print("Number in reverse order ->", result)
