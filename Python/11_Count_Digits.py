n = int(input("Enter a number: "))

# Logic for counting digits in the number

count = 0

while n > 0:
    n = n // 10
    count = count + 1

print(f"No of digits are = {count}")