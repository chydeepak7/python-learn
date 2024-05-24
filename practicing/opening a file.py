file_path = "input.py"  # Path to the file

# Open the file in read mode
with open(file_path) as file:
    # Read the contents of the file
    file_contents = file.read()
    print(file_contents)

file_path = "example.txt"  # Path to the file

# Open the file in write mode
with open(file_path, "w") as file:
    # Write or rewrite data to the file
    file.write("Helldo, world!")

