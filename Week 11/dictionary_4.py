def main():
    grades = {
        "Syllabus Quiz":100.0,
        "Quiz 1": 98.6,
        "Test 1": 87.5,
        "Final Exam": 105.0
    }

    if 100.0 in grades:
        print("100.0 exists in grades")
    else:
        print("100.0 does not exists in grades")

    if "Quiz 1" in grades:
        print("Quiz 1 exists in grades")
    else:
        print("Quiz 1 does not exists in grades")

    if 100.0 in grades.values():
        print("100.0 exists in grades")
    else:
        print("100.0 does not exists in grades")

    if ("Test 1", 87.5) in grades.items():
        print("(\"Test 1\", 87.5) exists in grades")
    else:
        print("(\"Test 1\", 87.5) does not exists in grades")
    
    if ("Test 1", 70.5) in grades.items():
        print("(\"Test 1\", 70.5) exists in grades")
    else:
        print("(\"Test 1\", 70.5) does not exists in grades")

    
if __name__ == "__main__":
    main()
