import time

def list_printer(a_list):
    for item in a_list:
        print(item, end = ", ")
    print()

def dotdotdot():
    for i in range(3):
        print(".", end = "")
        time.sleep(0.5)
    print()

def main():
    list_of_grades = [98.5, 74.9, 80.0, 78.8, 80.0]

    list_printer(list_of_grades)

    print(f"The list has {len(list_of_grades)} list_of_grades")

    print(f"We have {list_of_grades.count(80.0)} 80.0s in the list")

    print(f"The first 80.0 in the list is located at index {list_of_grades.index(80.0)}")

    print("Lets reverse the grades list", end="")
    dotdotdot()

    list_of_grades.reverse() #.reverse() is able to change the list, so no return

    list_printer(list_of_grades)

    print("Lets sort the grades list in ascending order", end = "")
    dotdotdot()

    list_of_grades.sort()

    list_printer(list_of_grades)

    print("Lets sort the grades list in descending order", end = "")
    dotdotdot()

    list_of_grades.sort(reverse=True)

    list_printer(list_of_grades)

    print(list("10"))

    # This will crash, you can only convert values that can be converted
    # into a list 
    print(list(10)) 







if __name__ == "__main__":
    main()