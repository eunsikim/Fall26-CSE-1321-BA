def input_grade():
    grade = int(input("Enter your grade: "))
    while True:
        if 0 <= grade <= 100:
            return grade
        else:
            grade = int(input("Enter your grade: "))

def check_lowest(g1, g2):
    if g1 < g2:
        return g1
    elif g1 > g2:
        return g2

def quiz_avg():
    quiz_sum = 0
    lowest_quiz = 100

    for x in range(11):
        quiz_grade = input_grade() 
        # Assumption: after this line code, `quiz_grade` is a value between 0 and 100

        quiz_sum += quiz_grade

        lowest_quiz = check_lowest(lowest_quiz, quiz_grade)

    quiz_sum -= lowest_quiz

    return quiz_sum / 10

def test_policy(t1 = False, t2 = False, f = False):
    # Applying test policy for Test 1
    if t1 != False:
        if t1 > t2 and t1 > f:
            return t1
        elif t2 > t1 and t2 > f:
            return t2
        else:
            return f
    else:
        if t2 > f:
            return t2
        else:
            return f

def input_bonus():
    visits =float(input("How many times have you been to the tutoring center?: "))
    while visits <= 10:
        bonus_sum = visits * 0.5
        return bonus_sum
    else:
        bonus_sum = 5
        return bonus_sum

def final_grade(q, t1, t2, f):
    return 0.25 * (q + t1 + t2 + f)

def convert_letter_grade(num_grade):
    if num_grade >= 89.5:
        return "A"
    elif num_grade >= 79.5:
        return "B"
    elif num_grade >= 69.5:
        return "C"
    elif num_grade >= 59.5:
        return "D"
    else:
        return "F"

def print_grade(grade_num, grade_let):
    print(f"Your CSE 1321 Final Grade is: {grade_num} ({grade_let})")