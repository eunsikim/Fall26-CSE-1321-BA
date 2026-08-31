def main():
    # The input function will:
    # 1. Prompt the string argument
    # 2. Wait for user response (press Enter)
    # 3. Return/Evaluate the input expression to the value inputted
    user_name = input("Enter your name: ")

    print("Hello", end=" ") # print
    # " " is a single Empty space
    # "" is Nothing/Empty string
    print(user_name) # print line/print new line

if __name__ == "__main__":
    main()