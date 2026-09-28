def main():
    # The range function generates a sequence
    # of numbers
    print(list(range(10))) # 10 is the EXCLUSIVE end range and the start range is always INCLUSIVE 0

    # Since range() is a sequence, we can use a
    # for loop to "iterate" through those numbers
    for number in range(10):
            print(number)

    # Range function with just end parameter (single)
    print(list(range(10))) # [0, 10) => [0, 9]

    # Range function with start and end parameters (double)
    print(list(range(100, 201))) # [100, 201) => [100, 200]

if __name__ == "__main__":
    main()