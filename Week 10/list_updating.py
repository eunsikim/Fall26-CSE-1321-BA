def main():
    grades = [98.5, 74.9, 80.0] 

    index = 0

    print("Select the index that you want to change:")
    for grade in grades:
        print(f"index {index}: {grade}")
        index += 1

    while True:
        index_choice = int(input("> "))

        if index_choice >= 0 and index_choice < len(grades):
            break
        else:
            print("Please enter a valid index")

    print()

    new_grade = float(input("What is the new grade: "))

    grades[index_choice] = new_grade

    print()

    print("This is the update grades list:")
    for grade in grades:
            print(grade)


if __name__ == "__main__":
    main()