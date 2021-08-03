# I knew the prompt in input already so I will just do the exercise
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# why is the following not working
# inside the print function input is first called, and then print is run? 
print("How old are you?", input())
