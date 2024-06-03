num = int(input("Enter a number: "))
result = 0

print(f"Number before reversed: {num}")

# Logic for Reverse a Number
while num > 0:
    digit = num % 10
    result = result * 10 + digit
    num = num // 10

num = result

print(f"Number after reversed: {num}")