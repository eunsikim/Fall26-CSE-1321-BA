def main():
    grades = [] # Initialize an empty list with `[]`

    print(grades)

    # `append()` adds a new value at the end of the list
    grades.append(90)

    print(grades)

    grades.append(80)

    print(grades)

    # `insert()` adds a new value at a specified index
    grades.insert(0, 75)
    print(grades)

    grades.insert(1, 70)
    print(grades)

    grades.insert(4, 88)
    print(grades)

    # `insert()` will add 78 at the next available index, not at 10
    grades.insert(10, 78)
    print(grades)

    grades.insert(10, 65)
    print(grades)

    # Lists can contain multiple data types
    grades.insert(7, "Hello World")
    print(grades)

if __name__ == "__main__":
    main()