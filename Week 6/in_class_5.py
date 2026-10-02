# Character Censoring Program
# Create a character censoring program
# where the user can input a sentence
# and a character they dislike
# the program should be able to reply
# with the same sentence/string
# but with the censored character replaced
# as an "*"

# Sample output:
# Enter a sentence: Hello World
# What character you do not like: o
#
# Hell* W*rld

# DO NOT USE THE .REPLACE()

sentence = input("Enter a sentence: ")
blocked_character = input("What character dont you like?: ")

for x in sentence:
    if x == blocked_character:
        print("*", end="")
    else:
        print(x, end="")


