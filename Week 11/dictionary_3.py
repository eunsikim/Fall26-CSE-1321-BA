def main():
    grades = {
        "Syllabus Quiz":100.0,
        "Quiz 1": 98.6,
        "Test 1": 87.5,
        "Final Exam": 105.0
    }

    # Iterating through a dictionary, 
    # will iterate through its keys
    for x in grades:
        print(x)

    print()

    for key in grades:
        print(grades[key])

    print()

    for key in grades:
        print(f"{key} {grades[key]}")

    print()

    # Special functions:
    # - Iterating by value
    for value in grades.values():
        print(value)

    print()

    # - Iterating by Key-Value Pair
    for entry in grades.items():
        print(entry)

    print()
    # - Iterating by Key
    for key in grades.keys():
        print(key)
    
if __name__ == "__main__":
    main()
