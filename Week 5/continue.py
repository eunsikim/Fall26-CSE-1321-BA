def main():
    end = int(input("Enter a number: "))

    current = 1

    while current <= end:
        if current % 3 == 0 and current % 5 == 0:
            print("FizzBuzz")
        elif current % 3 == 0:
            print("Fizz")
        elif current % 5 == 0:
            print("Buzz")
        else:
            if current == 7:
                current += 1
                continue # Will forcefully skip to the next iteration/repetition
            print(current)
            
        current += 1

if __name__ == "__main__":
    main()