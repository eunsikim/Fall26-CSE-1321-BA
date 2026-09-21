# - Ask the user to enter a number.
# - The program will print out a sequence of number starting 
#   from 1 and ending at the value the user inputs
# - For every number divisible by three, the program prints 
#   "Fizz" instead of the number
# - For every number divisible by five, the program prints
#   "Buzz" instead of the number
# - For every number divisible by both three and five, the program
#   prints "FizzBuzz" instead of the number

# Sample output:
"""
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
"""

def main():
    end = int(input("Enter a number: "))

    current = 1

    while current <= end:
        if current % 3 == 0 and current % 5 == 0:
            print("FizzBuzz")
        elif current % 3 == 0:
            print("Fizz")
        elif current % 5 == 0:
            print("Buzz")
        else:
            print(current)
            
        current += 1

if __name__ == "__main__":
    main()