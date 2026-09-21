def main():
    while True:
        print("1 - Print Hello World")
        print("Q - To stop")
        user_choice = input("> ")

        if user_choice == "1":
            print("Hello World")
        elif user_choice == "Q":
            print("Stopping the program...")
            break # Will forcefully STOP the loop
        else:
            print("Please enter either 1 or N")
    print("[Program Terminated]")

if __name__ == "__main__":
    main()