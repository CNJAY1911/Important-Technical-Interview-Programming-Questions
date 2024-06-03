num = int(input("Enter the number: "))

# Logic to check whether the number is Palindrome or not.

temp_num = num
reverse_num = 0

while temp_num > 0:
    remainder = temp_num % 10
    reverse_num = (reverse_num * 10) + remainder
    temp_num = temp_num // 10

if num == reverse_num:
    print(f"{num} - is a Palindrome")
else:
    print(f"{num} - is not a Palindrome")