def main():
    sentinel = "" # Sentinel values are values we define to signal the loop to stop

    while sentinel != "Q":
        print("1 - Print Hello World")
        print("Q - To stop")
        sentinel = input("> ")

        if sentinel == "1":
            print("Hello World")
        elif sentinel == "Q":
            print("Stopping the program...")
        else:
            print("Please enter either 1 or N")
    print("[Program Terminated]")

if __name__ == "__main__":
    main()