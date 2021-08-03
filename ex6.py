# define a variable called types_of_people and set its value to 10
types_of_people = 10
# def a var x and set its value to a format string
x = f"There are {types_of_people} types of people."

# def more vars
binary = "Binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# print the two format strings
print(x)
print(y)

# print format string with a format string inside
print(f"I said: {x}")
# the sigle quote inside is just a symbol surrounding the var y
print(f"I also said: '{y}'")

hilarious = False
# we can have a place holder empty {} inside of a string
joke_evaluation = "Isn't that joke so funny?! {}"

# we can use the .format method to replace all place holders with the argument
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# we can use the + sign to can catenate strings, to make one long string
print(w + e)
