# Prompt the user to input names
BoyName = input("Enter boy's name: ")
girlName = input("Enter girl's name: ")

# Convert names to lowercase
BoyName = BoyName.lower()
girlName = girlName.lower()

# Combine the names
combine = BoyName + girlName

# Count occurrences of letters
t = combine.count("t")
r = combine.count("r")
u = combine.count("u")
e = combine.count("e")
true = t + r + u + e

l = combine.count("l")
o = combine.count("o")
v = combine.count("v")
e = combine.count("e")
love = l + o + v + e

# Print the result
print(f"{true}{love}%")

# extra
# true_count = sum(combined_names.count(letter) for letter in true_letters)
# love_count = sum(combined_names.count(letter) for letter in love_letters)

# # Calculate the percentage of "true love"
# percentage = (true_count + love_count) % 100