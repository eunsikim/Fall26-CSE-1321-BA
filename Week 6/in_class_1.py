# Ask the user for two INTEGER number
# The program should perform an addition
# But you can only use the addition (+)
# operator with the integer 1.
# HINT: 1 + 2 => 1 + 1 + 1
# HINT: 2 + 3 => 1 + 1 + 1 + 1 + 1

def main():
    num1 = int(input("number 1: "))
    num2 = int(input("number 2: "))

    addition = 0

    for x in range(num1):
        addition += 1
        
    for x in range(num2):
        addition += 1

    print(f"{num1} + {num2} = {addition}")


if __name__ == "__main__":
    main()