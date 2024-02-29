import random

# Prompt the user to input their choice
user = int(input("Enter your choice (0 for 'Rock', 1 for 'Paper', 2 for 'Scissor'): "))

# Generate a random choice for the computer
computer = random.randint(0, 2)

# Print user and computer choices
print("User choice is ", user)
print("Computer choice is ", computer)

# Determine the winner based on the choices
if user == computer:
    print("No result, because you both have the same choice.")
elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    # In these cases, user wins
    print("You win!")
else:
    # Otherwise, computer wins
    print("You lose.")

# Comment to explain the logic:
# If the user's choice is the same as the computer's choice, it's a tie.
# Otherwise, we check the cases where the user wins:
# Rock (0) beats Scissors (2), Paper (1) beats Rock (0), and Scissors (2) beats Paper (1).
# If none of the above conditions are true, it means the computer wins.
