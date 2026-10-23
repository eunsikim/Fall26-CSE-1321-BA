"""
Create a program that asks the user for a sentence, then asks 
the user for a single character.

The program should check if the character exists in the sentence
and print TRUE or FALSE

You are not allowed to use the `in` or `contains` statements
to check if the character exist in the string

Sample output:
String: Hello World
Character: T
FALSE

Sample output:
String: Hello World
Character: e
TRUE
"""

import time

sentence = input("Enter a sentence: ")
char = input("Enter a character: ")

blank = False

for x in range(len(sentence)):
    print(f"if char:{char} == sentence[{x}]:{sentence[x]}?")
    time.sleep(0.25)
    if char == sentence[x]:
        print("Yes")
        blank=True
        time.sleep(0.25)
        break
    else:
        print("No, lets keep looking")
        time.sleep(0.25)
        blank=False

print()
print(blank)

