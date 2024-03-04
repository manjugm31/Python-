import os

# Function to find the winner from the bidders dictionary
def findWinner(bidders):
    height_bid = 0  # Initialize the highest bid
    winner = ""     # Initialize the name of the highest bidder

    # Iterate through each bidder in the dictionary
    for bidder in bidders:
        bid_amount = bidders[bidder]  # Get the bid amount for the current bidder

        # Check if the current bid amount is higher than the highest bid
        if bid_amount > height_bid:
            height_bid = bid_amount  # Update the highest bid
            winner = bidder          # Update the name of the highest bidder

    # Print the name of the highest bidder and their bid amount
    print(f"The name of the highest bidder is {winner} and the bid amount is {height_bid}")

# Initialize an empty dictionary to store the bidders and their bids
bidders = {}

end = False  # Initialize the end flag to control the loop

# Loop to collect bidder information until there are no more bidders
while not end:
    print("Welcome to bedding")
    name = input("Enter name: ")
    amount = int(input("Enter amount: "))

    # Add the bidder and their bid amount to the dictionary
    bidders[name] = amount

    # Ask if there is another person to bid
    next_person = input("Is there another person to bid? (yes/no): ")

    # Check if the bidding process should end
    if next_person.lower() == "no" or next_person.lower() == "not":
        end = True
        findWinner(bidders)  # Find the winner if bidding process ends
    elif next_person.lower() == "yes" or next_person.lower() == "there":
        os.system('cls')  # Clear the screen for the next bidding process
