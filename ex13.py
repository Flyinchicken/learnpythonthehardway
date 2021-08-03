# a script is another name of a .py file

# import allows you to add features to your script from the python feature set
# import what you need when you need it keeps the program small
from sys import argv # argv is the argument variable
# this argv variable holds what you pass to the script when you run it
# these small features we import are called "modules" or "libraries"

# read the WYSS section for how to run this
script, first_name, last_name = argv
# here we 'unpacked' the argument and separate them and store them in 4 variables

print("The script is called:", script)
print("Your script {} is run by {} {}".format(script, first_name, last_name))
number = input(f"What's your favorite number {first_name} {last_name}? ")
print(f"Nice {first_name} {last_name}! I like the number {number} too!")
