# This program will print a range of numbers
# The program will ask the user for a starting number
# and the ending number
# For example, if the user enters 1 and 5, the program
# should output: 1, 2, 3, 4, 5

def main():
    start = int(input("Enter starting value: ")) 
    end = int(input("Enter ending value: ")) 

    current_number = start 

    while current_number <= end: 
        print(f"{current_number}, ", end="") 
        current_number += 1 
        # current_number = current_number + 1 # This is the equivalent of the line above

    print()

    print("[Program Terminated]")

if __name__ == "__main__":
    main()