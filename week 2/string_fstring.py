# This program is an update to "input_2.py"
def main():
    user_name = input("Enter your name: ")
    year_born = int(input("What year were you born?: "))

    age = 2026 - year_born

    # Concatenation
    print("Hello " + user_name)

    print("You are " + str(age) + " years old.")

if __name__ == "__main__":
    main()