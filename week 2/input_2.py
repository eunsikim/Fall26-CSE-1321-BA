def main():
    user_name = input("Enter your name: ")
    year_born = int(input("What year were you born?: ")) # input() will always resolve into a string
    # Order of operations:
    # 1. year_born = int(input("What year were you born?: "))
    # 2. year_born = int("1996")
    # 3. year_born = 1996

    age = 2026 - year_born

    print("Hello", end=" ")
    print(user_name)

    print("You are", end=" ")
    print(age, end=" ")
    print("years old.")

if __name__ == "__main__":
    main()