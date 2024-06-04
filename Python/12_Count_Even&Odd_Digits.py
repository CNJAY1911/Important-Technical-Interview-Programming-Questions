n = int(input("Enter a number: "))

# Logic for Counting Even/Odd digits in the given number

even_count = 0
odd_count = 0

while n > 0:
    if(n % 2 == 0):
        even_count += 1
    else:
        odd_count += 1
        
    n = n // 10

print(f"Even Numbers: {even_count}")
print(f"Odd Numbers: {odd_count}")