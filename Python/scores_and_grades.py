import random

def grade_generator():
    print "Scores and Grades"
    for each in range(10):
        score = random.randint(60,100)
        if score >=90:
            grade = "A"
        elif score >=80:
            grade = "B"

        elif score >=70:
            grade = "C"

        elif score >=60:
            grade = "D"

        print "Score:", str(score) + ";", "Your grade is", grade
    print "End of program. Bye!"

grade_generator()
