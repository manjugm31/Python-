# Get the starting number from the user
start = int(input("Enter starting number: "))
# Get the ending number from the user
end = int(input("Enter last number: "))

# Loop through the numbers from the starting number (inclusive) to the ending number (exclusive)
for i in range(start, end):
    # Check if the number is divisible by both 3 and 5
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    # Check if the number is divisible by 3
    elif i % 3 == 0:
        print("Fizz")
    # Check if the number is divisible by 5
    elif i % 5 == 0:
        print("Buzz")
    # If none of the conditions are met, print the number itself
    else:
        print(i)
