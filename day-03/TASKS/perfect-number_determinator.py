# Write the code ↓ to read the user's input for a positive integer.
# Be cautious when reading input of various data types.

print("\n--------------------------")
print("\nPERFECT NUMBER CHECKER\n")

while True:
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Error: Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Error: Please enter a valid positive integer.")

# Write the code ↓ to check if the entered integer is a Perfect Number using a loop.

divisor_sum = 0
for i in range(1, num):
    if num % i == 0:
        divisor_sum += i

is_perfect = divisor_sum == num

# Write the code ↓ to display the Perfect Number check result.
# NOTE : You can use if-else statement or ternary operator to display the result.

result = "is a Perfect Number." if is_perfect else "is not a Perfect Number."

print("\n--------------------------")
print(f"The number {num} {result}")