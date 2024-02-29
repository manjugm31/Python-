n = int(input("Enter a number: "))  # Prompting the user to enter a number and converting it to an integer
total_sum = 0  # Variable to store the sum of digits
while n > 0:
    digit = n % 10  # Extracting the last digit of the number
    total_sum += digit  # Adding the digit to the total sum
    n = n // 10  # Removing the last digit from the number by integer division
print("The sum of digits:", total_sum)  # Printing the sum of digits
