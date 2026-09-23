# Count how many vowels I have in `message`
# You cannot use the len() function

def main():
    message = "Hello World"

    count = 0

    # We change the characters in `message`
    # to uppercase to make the program
    # case-insensitive
    message = message.upper()

    for character in message:
        # character == "a" or "e" or "i" or "o" or "u" THIS IS NOT LEGAL
        # Each expression is a unique expression
        
        if character == "A" or character == "E" or character == "I" or character == "O" or character == "U":
            count += 1
    
    print(f"'{message}' has {count} vowels")

if __name__ == "__main__":
    main()