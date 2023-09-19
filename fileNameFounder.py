# Input the filename from the user
filename = input("Enter a filename: ")

# Split the filename to get the file extension
file_extension = filename.split(".")[-1]

# Print the file extension without the dot
print(f"The file extension is: {file_extension}")
