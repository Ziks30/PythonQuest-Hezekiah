import math

# Write the code ↓ to read the lengths of the two shorter sides of a right-angled triangle from the user.
# Be cautious when reading input of various data types.

print("\n--------------------------")
print("\nHYPOTENUSE CALCULATOR\n")

while True:
    try:
        side1 = float(input("Enter the length of the first shorter side: "))
        side2 = float(input("Enter the length of the second shorter side: "))
        break
    except ValueError:
        print("Error: Please enter valid floating-point numbers.")

# Write the code ↓ to calculate the hypotenuse using the Pythagorean theorem.
# The Pythagorean theorem: c^2 = a^2 + b^2, where c is the hypotenuse.

hypotenuse = (side1 ** 2 + side2 ** 2) ** 0.5

# Write the code ↓ to display the calculated hypotenuse.
# Select and employ a string concatenation method based on your personal preference and comfort level.

print("\n--------------------------")
print("The hypotenuse of the right-angled triangle is: {:.2f}".format(hypotenuse))