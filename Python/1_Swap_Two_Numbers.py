num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))

print("Before swapping:")
print(f"num1 = {num1}")
print(f"num2 = {num2}")

# Swapping Logic:
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping:")
print(f"num1 = {num1}")
print(f"num2 = {num2}")