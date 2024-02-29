# Prompt the user to input weight and height
weight = float(input("Enter the weight (in kilograms): "))
height = float(input("Enter the height (in meters): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Check BMI category and print the result
if bmi <= 18.5:
    print("Underweight because your BMI =", bmi)
elif bmi <= 24.9:  # BMI range for Normal weight
    print("Normal weight because your BMI =", bmi)
elif bmi <= 29.9:  # BMI range for Overweight
    print("Overweight because your BMI =", bmi)
else:  # BMI range for Obese
    print("Obese because your BMI =", bmi)
