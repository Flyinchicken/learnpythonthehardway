# import argv to use the argument variable
from sys import argv
# set two variables for the first two argv, use the argv to get filename from the user
script,filename = argv

# open function takes the filename and return a file object
# the file object is a path-like object (pathname)
txt = open(filename)

# defines the prompt which can be changed globally if needed
prompt = "> "

# print this formatted string: info of the file
print(f"Here's your file {filename}:")
# txt.read() returns the content of the file as text and then print it
print(txt.read())

# ask for a filename and save it to file_again
print("Type the filename again:")
file_again = input(prompt)

# open the file named as file_again
txt_again = open(file_again)

# .read method to get the content and then print the content
print(txt_again.read())

# close files when finished
txt.close()
txt_again.close()
