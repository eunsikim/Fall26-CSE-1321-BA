def main():
    student_grade = {
        "Quiz":[],
        "Test":[],
        "Final Exam":0
    }

    # Quiz Input
    for x in range(10):
        quiz_grade = float(input(f"Enter grade for Quiz {x + 1}: "))

        student_grade["Quiz"].append(quiz_grade)

    # Test Input
    for x in range(2):
        test_grade = float(input(f"Enter grade for Test {x + 1}: "))

        student_grade["Test"].append(test_grade)

    final_exam_grade = float(input("Enter grade for Final Exam: "))
    student_grade["Final Exam"] = final_exam_grade

    print(student_grade)

    # TODO: Calculate the quiz average

    # TODO: Calculate the Final Grade
    
if __name__ == "__main__":
    main()