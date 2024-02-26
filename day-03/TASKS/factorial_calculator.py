# Write the code ↓ to read the user's input for a non-negative integer.
# Be cautious when reading input of various data types.

print("\n--------------------------")
print("\nFACTORIAL CALCULATOR FOR ALF\n")

while True:
    try:
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("Error: Please enter a non-negative integer.")
        else:
            break
    except ValueError:
        print("Error: Please enter a valid non-negative integer.")

# Write the code ↓ to calculate the factorial of the user-defined integer using a loop.

fact = 1
for i in range(1, n + 1):
    fact *= i

# Write the code ↓ to display the factorial result.
# Select and employ a string concatenation method based on your personal preference and comfort level.

print("\n--------------------------")
print(f"The factorial of {n} is: {fact}")