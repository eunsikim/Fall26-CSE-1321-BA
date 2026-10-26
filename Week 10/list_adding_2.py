def main():
    grades = [] # Initialize an empty list with `[]`

    quiz_amount = int(input("How many quizzes do you have?: "))

    for x in range(quiz_amount):
        quiz_grade = float(input(f"Enter grade for Quiz {x + 1}: "))
        grades.append(quiz_grade)

    print(grades)

    quiz_sum = 0

    for x in range(quiz_amount):
        quiz_sum += grades[x]

    quiz_average = quiz_sum / quiz_amount

    print(f"Your quizz average is: {quiz_average:.2f}")

if __name__ == "__main__":
    main()