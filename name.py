# Get input from the user
names_input = input("Enter names separated by commas: ")

# Split the input string into a list of names
names_list = names_input.split(",")

# Open the file in append mode
with open("names.txt", "a") as file:
    # Write each name to the file
    for name in names_list:
        file.write(name.strip() + "\n")  # Add a newline after each name

print("Names have been written to names.txt")
