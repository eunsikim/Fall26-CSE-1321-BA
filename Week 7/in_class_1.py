# Letter Grade Converter
# Define a function called `convert_grade()` which
# takes in one parameter (a numeric grade). The 
# function should then convert this value into a 
# letter grade and return it.
# 
# Letter Grade Scale:
# A > 89
# B > 79
# C > 69
# D > 59
# F <= 59

def get_letter_grade(grade):
    if grade>89:
        return "A"
    elif grade>79:
        return "B"
    elif grade>69:
        return "C"
    elif grade>59:
        return "D"
    else:
        return "F"


def grade_validator():
    grade = float(input("Enter Your Grade: "))

    if 0 <= grade <= 100:
        return grade

    return -1


def main():
    grade = grade_validator()

    if grade != -1:
        letter_grade = get_letter_grade(grade)
        print(f"{grade} is a {letter_grade} letter grade")
    else:
        print(f"That is not a valid grade.")

if __name__ == "__main__":
    main()
