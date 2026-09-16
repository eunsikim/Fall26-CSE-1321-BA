"""
Login System:
- The program should take in a username and password from the user and evaluate if the login is valid or not.
- The program should output if a login is successful, if not it should output whether the password or 
  username was invalid.
- The hardcoded username is “admin”, and the password is “password123”
- The username and password input should be case sensitive.
"""

def main():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "admin" and password == "password123":
        print("Login Successful!")
    else: # 
        if username == "admin":
            print("The password is incorrect")
        elif password == "password123":
            print("The username is incorrect")
        else:
            print("Username and Password are incorrect")

if __name__ == "__main__":
    main()