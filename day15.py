# Generate a string
original_string = "I love programming in Python"

# Convert to uppercase
original_string = original_string.upper()

# Convert string to a list of characters
original_list = list(original_string)

# Swap the position of adjacent characters
for i in range(0, len(original_list)-1, 2):
    original_list[i], original_list[i+1] = original_list[i+1], original_list[i]

# Convert the list back to a string
swapped_string = "".join(original_list)

# Print the result
print(swapped_string)
