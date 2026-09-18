def main():
    num1 = float(input("Enter a number: "))
    op = input("Enter an op: ")
    num2 = float(input("Enter a number: "))

    while op == "/" and num2 == 0:
        print("We cannot do division by zero, try again.")
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