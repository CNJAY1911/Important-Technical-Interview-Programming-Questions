from math import pow

### If We took input as a string ###

n = input("Enter a number: ")
power = len(n)

# Logic for checking Armstrong number
sum = 0
for i in n:
    sum += pow(int(i), power)

if sum == int(n):
    print("Yes")
else:
    print("No")



### If We took input as an integer ###

'''

n = int(input("Enter a number: "))
power = len(str(n))

# Logic for checking Armstrong number
sum = 0
temp_num = n

while temp_num > 0:
    sum += pow(temp_num % 10, power)
    temp_num //= 10

if sum == n:
    print("Yes")
else:
    print("No")

'''