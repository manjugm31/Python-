# Take input from the user
input_str = input("Enter the numbers separated by spaces: ")

# Print the input and its type
print("Input:", input_str)
print("Type:", type(input_str))

# Split the input into a list of strings
input_list = input_str.split(" ")

# Print the list of strings
print("List of strings:", input_list)

# Count the number of elements in the list
count = len(input_list)
print("Count:", count)

# Convert each string element to an integer
for j in range(count):
    input_list[j] = int(input_list[j])
print("List of integers:", input_list)

# Bubble sort algorithm implementation
for k in range(count):
    for l in range(0, count - k - 1):
        if input_list[l] > input_list[l + 1]:
            # Swap elements if they are in the wrong order
            temp = input_list[l]
            input_list[l] = input_list[l + 1]
            input_list[l + 1] = temp

# Print the sorted list
print("Sorted list:")
print(input_list)
