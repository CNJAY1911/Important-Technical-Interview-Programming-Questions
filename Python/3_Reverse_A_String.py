word = input("Enter the String: ")
result = ""
print(f"String before reversed: {word}")

# Logic for Reversing a String
for i in range(len(word) - 1, -1, -1):
    result += word[i]

word = result
print(f"String after reversed: {word}")