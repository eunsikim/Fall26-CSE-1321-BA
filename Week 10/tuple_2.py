def get_user_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    return name, age

def get_average(*grades):
    average_sum = 0

    for grade in grades:
        average_sum += grade

    return average_sum / len(grades)

def main():
    # response_tuple = get_user_info()

    # print(f"Hello {response_tuple[0]}, you are {response_tuple[1]} years old.")

    user_name, user_age = get_user_info()

    print(f"Hello {user_name}, you are {user_age} years old.")

    print(f"Your average is: {get_average(100, 100, 50, 90, 100, 34, 84)}")


if __name__ == "__main__":
    main()