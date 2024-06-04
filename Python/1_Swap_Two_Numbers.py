num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))

print("Before swapping:")
print(f"num1 = {num1}")
print(f"num2 = {num2}")

# Logic for Swapping 2 numbers without using 3rd variable

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

# Logic for Swapping 2 numbers using 3rd variable

'''
temp = num1
num1 = num2
num2 = temp
'''

print("After swapping:")
print(f"num1 = {num1}")
print(f"num2 = {num2}")