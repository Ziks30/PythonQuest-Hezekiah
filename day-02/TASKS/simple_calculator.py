# Write the code ↓ to read user's input for two operands and selected operation.
# NOTE: The two operands must be read as floats.

print("\n--------------------------")
print("\nSIMPLE CALCULATOR FOR ALF\n")

operand1 = float(input("Enter the first operand: "))
operand2 = float(input("Enter the second operand: "))

operation = input("Choose the operation (+, -, x, /): ")

# Write the code ↓ to perform the calculations based on the selected operation.

if operation == '+':
    result = operand1 + operand2
elif operation == '-':
    result = operand1 - operand2
elif operation == 'x':
    result = operand1 * operand2
elif operation == '/':
    if operand2 != 0:
        result = operand1 / operand2
    else:
        print("Error: Division by zero!")
 
# Write the code ↓ to display the result.
# Select and employ a string concatenation method based on your personal preference and comfort level.

print("\n--------------------------")
if result is not None:
    print("Result:", operand1, operation, operand2, "=", result)