"""
Calculator:
- Use match statements
- Ask the user to enter a number.
- Ask the user to enter an operation (+, -, *, or /).
- Ask the user to enter a second number.
- Based on the user select operation, perform the 
  corresponding operation and display the result.
"""

def main():
    num1 = float(input("Enter a number: "))
    op = input("Enter an op: ")
    num2 = float(input("Enter a number: "))

    match op:
        case "+":
            calc = num1 + num2
        case "-":
            calc = num1 - num2
        case "*":
            calc = num1 * num2
        case "/":
            calc = num1 / num2

    print(f"= {calc}")

if __name__ == "__main__":
    main()