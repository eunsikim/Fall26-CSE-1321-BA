def main():
    grades = [98.5, 74.9, 80.0] 
    print(grades[1])
    print(grades)

    # Delete by index
    del grades[1]

    print(grades)
    print(grades[1])

    # Delete the first item/element
    grade_just_deleted = grades.pop(0)
    print(grades)
    print(grade_just_deleted)

    # Re adding some values into the list
    grades.append(50)
    grades.append(80.0)
    print(grades)

    # Delete by item/element
    grades.remove(80.0)
    print(grades)

    # Delete all elements
    grades.clear()
    print(grades)


if __name__ == "__main__":
    main()