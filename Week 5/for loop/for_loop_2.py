# Count how many character I have in `message`
# You cannot use the len() function

def main():
    message = "Hello World"

    count = 0

    for character in message:
        count += 1
    
    print(f"'{message}' has {count} characters")

if __name__ == "__main__":
    main()