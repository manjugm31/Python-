import math

# Function to calculate the number of cans of paint required to paint a wall
def Paint_calculator(height, weight, coverage):
    # Calculate the total area of the wall
    area = height * weight
    
    # Calculate the number of cans required, rounding up to the nearest whole number
    can_required = math.ceil(area / coverage)
    
    # Print the result
    print(f"Number of cans of paint required to paint the wall is {can_required}")

# Prompting the user to input the dimensions of the wall and calling the function
height = int(input("Enter the height of the wall: "))
weight = int(input("Enter the weight of the wall: "))
coverage = 7  # Assuming coverage of 7 square units per can of paint

# Calling the Paint_calculator function with user inputs and coverage
Paint_calculator(height, weight, coverage)
