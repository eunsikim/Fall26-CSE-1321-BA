def a_password(text):
    if len(text) >= 8:
        return True
    else:
        return False

def validate_password(password):
    if a_password(password):
        print("Valid password")
    else:
        print("Invalid password")

def main():
    password = input("Enter a password: ")

    validate_password(password)

if __name__ == "__main__":
    main()