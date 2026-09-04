def main():
    # Any time you have a `int OP int` it will result in another int
    print(type(3 + 7))

    # Any time you have a `float OP int`  or vice-versa, it will result in a float
    print(type(3.0 + 7))
    print(type(3 + 7.0))

    # Any time you have a `float OP float` it will result in another float
    print(type(3.0 + 7.0))

    print()

    # This behavior works for all arithmetical operators 
    # except Division
    print(type(3 / 7))
    print(type(3.0 / 7))
    print(type(3 / 7.0))
    print(type(3.0 / 7.0))

    print()

    # Comparison Operators
    print(3 == 7)
    print(3 != 7)
    print(3 > 7)
    print(3 >= 7)
    print(3 < 7)
    print(3 <= 7)

    print()

    print(3 < 3)
    print(3 <= 3)

    # When comparing strings, the == operator is case sensitive
    print("Hello" == "hello")
    print("Hello" == "Hello")

    


if __name__ == "__main__":
    main()