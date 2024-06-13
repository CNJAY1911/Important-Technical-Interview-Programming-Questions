'''
Write a function to calculate the sum of even numbers in a 
given list of integers. The function should take a list of
integers as input and return the sum of all even numbers
in the list.

Input: numbers (1 <= len(numbers) <= 1000) : A list of integers
Output: Return an integer representing the sum of all even numbers in the list.

For example, 
Input: [1,2,3,4,5,6]
# Output: 12 (2 + 4 + 6 = 12)
'''

def sum_of_even_numbers(numbers):
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum += num
    return sum

numbers = [1,2,3,4,5,6]

print(sum_of_even_numbers(numbers))