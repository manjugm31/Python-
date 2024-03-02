# Define the alphabet list
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Function to encrypt the text
def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        # Find the position of the character in the alphabet
        position = alphabet.index(char)
        # Calculate the new position after adding the key
        new_position = (position + key) % 26
        # Append the encrypted character to the encrypted text
        encrypted_text += alphabet[new_position]
    # Print the encrypted text
    print("Encrypted text:", encrypted_text)

# Function to decrypt the text
def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        # Find the position of the character in the alphabet
        position = alphabet.index(char)
        # Calculate the new position after subtracting the key
        new_position = (position - key) % 26
        # Append the decrypted character to the decrypted text
        decrypted_text += alphabet[new_position]
    # Print the decrypted text
    print("Decrypted text:", decrypted_text)

# Prompt the user for encryption or decryption
what_to_do = input("Encryption or Decryption: ")
text = input("Enter the message: ")
key = int(input("Enter the value, how much you need to move: "))

# Perform encryption or decryption based on user input
if what_to_do.lower() == "encryption":
    encrypt(text, key)
elif what_to_do.lower() == "decryption":
    decrypt(text, key)
else:
    print("Invalid input. Please enter 'Encryption' or 'Decryption'.")
