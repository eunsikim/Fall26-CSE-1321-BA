import random

class banking_account:
    # Constructor
    def __init__(self, name, dob, contact_info, email, password):
        self.name = name
        self.dob = dob
        self.contact_info = contact_info
        self.balance = 0.0
        self.email = email
        self.password = password
        self.account_num = random.randint(1000, 9999)

        print("A new banking account has been created.")

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("ERROR: There is no enough balance for this withdrawal")
        else:
            self.balance -= amount
            print("Withdrawal was successful!")

    def deposit(self, amount):
        if amount < 0:
            print("ERROR: Invalid deposit amount")
        else:
            self.balance += amount
            print("Deposit was successful!")

def main():
    users = []

    isLoggedIn = False

    while True:
        if not isLoggedIn:
            print("0 Open an account")
            print("1 Log in")
            print("X Exit")
        else:
            print("2 Withdraw")
            print("3 Deposit")
            print("4 Log Out")

        option_choice = input("> ")

        if option_choice == "0" and not isLoggedIn:
            name = input("Enter your name: ")

            # TODO: Enforce email uniqueness.
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            dob = input("Enter your dob: ")
            contact_info = input("Enter your contact info: ")

            new_user = banking_account(name, dob, contact_info, email, password)

            users.append(new_user)

            # DEV MODE: Print users:
            for user in users:
                print(user.name)

        elif option_choice == "1" and not isLoggedIn:
            pass
        elif option_choice == "2" and isLoggedIn:
            pass
        elif option_choice == "3" and isLoggedIn:
            pass
        elif option_choice == "4" and isLoggedIn:
            pass
        elif option_choice == "X" and not isLoggedIn:
            print("Terminating Program...")
            break


if __name__ == "__main__":
    main()