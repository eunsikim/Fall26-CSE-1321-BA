def main():
    # We can initialize a tuple with parentheses `()`
    grades = (90, 0)

    print(grades[0])

    # We cannot modify a value inside of a tuple
    # This line will crash
    grades[0] = 100

if __name__ == "__main__":
    main()