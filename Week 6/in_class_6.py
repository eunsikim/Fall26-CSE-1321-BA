# Diagonal Printer
# Ask the user for a sentence
# The program should print
# the same sentence, but instead
# of printing it horizontally,
# the print should be diagonally.

# Sample output:
# Enter a sentence: Hello
# H
#  e
#   l
#    l
#     o

# You must use nested loops (FOR)

sen = input("Enter a sentence: ")

count = 0 # The amount of spaces in a line

for char in sen:
    for i in range(count):
        print(" ", end= "")
    print(char)
    count += 1

