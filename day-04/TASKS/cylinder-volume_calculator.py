import math

# Write the code ↓ to read the radius and height of a cylinder from the user.
# Be cautious when reading input of various data types.

print("\n--------------------------")
print("\nCYLINDER VOLUME CALCULATOR\n")

while True:
    try:
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        if radius <= 0 or height <= 0:
            print("Error: Both radius and height must be positive numbers.")
        else:
            break
    except ValueError:
        print("Error: Please enter valid floating-point numbers.")

# Write the code ↓ to calculate the volume of the cylinder using the formula V = πr^2h.
# Formula to calculate the volume (V) of a cylinder:
# V = π * r^2 * h

volume = math.pi * radius ** 2 * height

# Write the code ↓ to display the calculated volume with 2 decimal places.
# Select and employ a string concatenation method based on your personal preference and comfort level.

print("\n--------------------------")
print("The volume of the cylinder is: {:.2f}".format(volume))