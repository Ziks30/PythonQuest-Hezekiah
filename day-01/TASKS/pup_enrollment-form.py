# Write the code ↓ to read user's input.
# Be cautious when reading input of various data types.

print("\n-----------------------")
print("\nWelcome to PUP Enrollment Form!\n")

name = input("Enter your full name: ")
age = int(input("Enter your age: "))
gwa = float(input("Enter your previous general weighted average: "))
membership = input("Are you a member of AWS Cloud Club? (yes/no): ")

# Converts string to boolean
membership = membership.lower() == 'yes'


# Write the code ↓ to display the user's personal information.
# Select and employ a string concatenation method based on your personal preference and comfort level.

print("\n-----------------------")
print("\nYour Enrollment Form:")
print("Name: " + name)
print("Age: " + str(age))  # Converts to string for concatenation
print("GWA: " + str(gwa))
print("Member of AWS Cloud Club: " + str(membership))