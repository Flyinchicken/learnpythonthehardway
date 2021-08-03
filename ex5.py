# everytime we put "" (double quote) around we make a string
# print string, send strings to server, save strings. Interaction between
# our program and outside
# To embeb variable we put {} inside the double quote ""
# format the string starting with f

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 * 2.54 # centimeters
weight = 180 * 0.453592 # kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He's {weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
# A mistake here, I got capitalized P for print and it cannot be recognized
