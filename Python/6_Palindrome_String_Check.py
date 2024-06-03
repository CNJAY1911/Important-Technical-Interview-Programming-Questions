word = input("Enter the String: ")

reverse_string = ""

# Logic for checking whether the input string is Palindrome or not.

for i in range(len(word) - 1, -1, -1):
    reverse_string += word[i]

if word == reverse_string:
    print(f"{word} - is a Palindrome")
else:
    print(f"{word} - is not a Palindrome")