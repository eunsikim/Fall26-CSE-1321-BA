"""
Number Categorizer
- Prompt the user for a number.
- The program should evaluate if the number is negative or zero. 
  If neither, it should check if the number is even or odd.
"""

def main():
    number = int(input("Enter a number: "))

    if number < 0:
        print(f"The number {number} is negative.")
    elif number == 0:
        print(f"The number {number} is zero.")
    else:
        if number % 2 == 0: # number is a positive and even number
            print(f"The number {number} is even.")
        else:
            print(f"The number {number} is odd.")


if __name__ == "__main__":
    main()