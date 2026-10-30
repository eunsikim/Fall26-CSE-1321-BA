def main():
    """
        Name    Grade
        Alice   90
        Bob     70
        Charlie 89
    """
    students = [["Alice", 90], ["Bob", 70, 90, 100, 89], ["Charlie", 89]]
    # students = [x, y, z]

    # Multi-step approach
    student_alice = students[0]
    print(f"{student_alice[0]} got a {student_alice[1]}")

    # One-step approach
    print(f"{students[0][0]} got a {students[0][1]}")

    print()

    print("Name\tGrade")
    print(f"{students[0][0]}\t{students[0][1]}")
    print(f"{students[1][0]}\t{students[1][1]}")
    print(f"{students[2][0]}\t{students[2][1]}")

    print()

    print("Name\tGrade")
    for student_index in range(len(students)):
        print(f"{students[student_index][0]}\t{students[student_index][1]}")

    print()
    print("Name\tGrade")
    for student_index in range(len(students)):
        for student_value_index in range(len(students[student_index])):
            print(f"{students[student_index][student_value_index]}\t", end = "")
        print()


if __name__ == "__main__":
    main()