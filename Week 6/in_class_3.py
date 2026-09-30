# Create a program that takes in a sentence 
# from the user, and asks how to split that
# sentence (delimiter) and then output
# the separated sentence.

# Sample output
# Enter a sentence: Hello,World,CSE,1321
# Enter a delimiter: ,
# 
# Split:
# Hello
# World
# CSE
# 1321

# Challenge: Find a away to make the delimiter more than 1 character long.
#            and work.

def main():
    string = input("Enter a sentence: ")
    delimiter = input("Enter a delimiter: ")

    for c in string:
        if c == delimiter:
            print()
        else:
            print(c, end="")
    print()

if __name__ == "__main__":
    main()