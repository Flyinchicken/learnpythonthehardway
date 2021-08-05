# def add(a, b):
#     print(f"ADDING {a} + {b}")
#     return a + b
#
# def subtract(a, b):
#     print(f"SUBTRACTING {a} - {b}")
#     return a - b
#
# def multiply(a, b):
#     print(f"MULTIPLYING {a} * {b}")
#     return a * b
#
# def divide(a, b):
#     print(f"DIVIDING {a} / {b}")
#     return a / b
#
#
# print("Let's do some math with just functions!")
#
# age = add(30, 5)
# height = subtract(78, 4)
# weight = multiply(90, 2)
# iq = divide(100, 2)
#
# print("Age: {}, Height: {}, Weight: {}, IQ: {}.".format(age, height, weight, iq))
#
#
# # A puzzle for the extra credit, type it anyway.
# print("Here is a puzzle.")
#
# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#
# print("That becomes: ", what, "Can you do it by hand?")

def force_elec(charge1, charge2, distance):
    return (8.98755 * (charge1 * charge2)) / (distance * distance)

q1 = 30
q2 = 25
r = 0.03

fc = force_elec(q1, q2, r)
print(fc)
