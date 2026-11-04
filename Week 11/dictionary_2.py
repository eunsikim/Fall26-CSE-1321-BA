def main():
    grades = {
        "Syllabus Quiz":100.0,
        "Quiz 1": 98.6,
        "Test 1": 87.5,
        "Final Exam": 105.0
    }

    print(grades)
    print()

    # Add a new entry into `grades{}`
    grades["Quiz 2"] = 78.8 

    print(grades)
    print()

    # Removing KV-Pairs in a dictionary
    del grades["Syllabus Quiz"]

    print(grades)
    print()

    print(f"Pop: {grades.pop("Test 1")}")
    print(grades)
    print()


    print(f"Pop Item: {grades.popitem()}")
    print(grades)
    print()

    # Modify/Update values in a dictionary
    grades["Quiz 1"] = 78.0
    print(grades)
    print()
    
if __name__ == "__main__":
    main()
