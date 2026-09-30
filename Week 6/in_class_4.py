# Create a program that takes in a sentence from the user
# and prints the exact sentence but each line is capped to
# 5 characters long
#
# Sample Output:
# Enter a sentence: Lorem Ipsum is simply
#
# Lorem
#  Ipsu
# m is 
# simpl
# y
#
# Challenge: Try to solve this without using %

def main():
    string = input("Enter a sentence: ")

    line_length = 20

    counter = 0

    for c in string:
        if counter % line_length == line_length - 1:
            print(c)
        else:
            print(c, end="")

        counter += 1
    print()

if __name__ == "__main__":
    main()