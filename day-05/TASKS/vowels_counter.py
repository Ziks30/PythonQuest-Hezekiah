# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.

print("\n--------------------------")
print("\nVOWEL COUNT PROGRAM\n")

word = input("Enter a word: ")

# Write the code ↓ to count the number of vowels in the entered word.
# Utilize string functions to iterate through the characters and identify vowels.

vowel_count = 0
vowels = {'a', 'e', 'i', 'o', 'u'}

for char in word.lower():
    if char in vowels:
        vowel_count += 1

# Write the code ↓ to display the count of vowels in the word.
# Select and employ a string concatenation method based on your personal preference and comfort level.

print("\n--------------------------")
print("The number of vowels in the word '" + word + "' is:", vowel_count)