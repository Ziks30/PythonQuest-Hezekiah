# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.

print("\n--------------------------")
print("\nSIMPLE PALINDROME CHECKER FOR ALF\n")

# Input a word from the user
word = input("Enter a word: ")

# Write the code ↓ to check if the entered word is a palindrome.
# Utilize string functions to compare the original word with its reverse.

if word.lower() == word.lower()[::-1]:
    palindrome_status = "is"
else:
    palindrome_status = "is not"

# Write the code ↓ to display whether the entered word is a palindrome or not.
# Select and employ a string concatenation method based on your personal preference and comfort level.

print("\n--------------------------")
print(f"The word '{word}' {palindrome_status} a palindrome.")
