# Create a program that outputs a python script
# Ask the user for a number
# The program should output the multiplication table
# the input number from 1 - 9
# YOU MUST USE LOOPS
# HINT: print('"hello"') => Output: "hello"

# Sample Output
# Enter a number: 9
#
# print("1 x 9 = 9")
# print("2 x 9 = 18")
# ...
# print("9 x 9 = 81")

def main():
    number = int(input("Enter a number: "))

    for x in range(9):
        print(f'print("{x + 1} x {number} = {(x + 1) * number}")')


if __name__ == "__main__":
    main()