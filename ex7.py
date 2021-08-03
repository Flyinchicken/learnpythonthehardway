print("Mary had a little lamb.")
# put place holders in a string and then use .format method to format things
# into the place holders
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")

# basically, multiplication by a number is cancatenating a string number of times
print("." * 10) # what'd that do?

end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing is to see what happen
# cancatenate all chars to make a word(string)
# with a comma, we can print different things
# without it we will get syntatic error
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
