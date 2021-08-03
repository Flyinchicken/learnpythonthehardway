# the end=' ' at the end tells the print function not to end with a new line
print("How old are you?", end=' ')

# the input() function takes an optional argument 'the prompt' and take the input
# from the user and convert it into a string
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

name = input("What's your name? ")
address = input("Hello {}, where do you live? ".format(name))
print("Ok {}, you live in {}.".format(name,address))
