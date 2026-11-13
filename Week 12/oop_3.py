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

    users.append( banking_account("John Doe", "11/13/2000", "Some contact", "jdoe01@students.kennesaw.edu", "1234") )

    users[0].withdraw(1000)
    users[0].deposit(500)
    users[0].deposit(-500)

    print(f"Balance: ${users[0].balance:.2f}")


if __name__ == "__main__":
    main()