# BMI - NUTRITIONAL STATUS GUIDE
"""
    BMI         NUTRITIONAL STATUS

BELOW 18.5         UNDERWEIGHT
18.5 - 24.9       NORMAL WEIGHT
25.0 - 29.9        OVERWEIGHT
ABOVE 30.0          OBESITY
"""
 
# Write the code ↓ to read user's height and weight.
# Be cautious when reading input of various data types.

print("\n--------------------------")
print("\nBMI CALCULATOR FOR ALF\n")

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

status = ""

# Write the code ↓ to perform the calculations of user's BMI and categorize its status.

bmi = weight / height**2

if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi < 25:
    status = "Normal Weight"
elif 25 <= bmi < 30:
    status = "Overweight"
elif bmi >= 30:
    status = "Obesity"

# Write the code ↓ to display the user's BMI and its classification.
# Select and employ a string concatenation method based on your personal preference and comfort level.
# Use :.2f format specifier when printing the BMI value to display the BMI with only two decimal places.

BMI = int(bmi)

print("\n--------------------------")

print("HEIGHT: " + str(height) + " meters")
print("WEIGHT: " + str(weight) + " kilograms")

print(f"BMI: {bmi:.2f}")
print("NUTRITIONAL STATUS: " + status) 