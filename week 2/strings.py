def main():
    message = "Hello CSE 1321"

    print(message)
    print(len(message))

    # These functions are temporary (single use)
    print(message.replace("l", "Goodbye"))
    print(message.lower())
    print(message.upper())
    print(message)

if __name__ == "__main__":
    main()