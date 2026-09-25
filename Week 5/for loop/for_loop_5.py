# Password Validator
# A valid password must:
# Be at least 8 characters long
# Must contain at least 1 special character: !, @, #
# Must contain at least 1 number
# 
# The program should ask the user for a password
# then output if the password is valid or not

def main():
    password = input("Enter your password: ")

    char_count = 0

    length_check = False
    special_char_check = False
    number_check = False

    # Check password length
    for character in password:
        char_count += 1

    if char_count >= 8:
            length_check = True
    
    # Check special characters

    # Check numerical characters

    if length_check and special_char_check and number_check:
        print("Valid")
    else:
        print("Not Valid")

if __name__ == "__main__":
    main()