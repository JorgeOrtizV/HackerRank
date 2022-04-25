# This program receives an integer n, which means the amount of grades the program will receive.
# The following numbers represents the grades from a students. The program output the grades with roundings or not roundings
# The grading criteria are the following:
# If the grade is less than 38 then no rounding is applied
# If the difference between the grade and the next multiple of 5 is less than 3, then the grade is rounded to the next
# multiple of 5

def rounder(grade):
    if grade < 38:
        print(grade)
        return
    else:
        if (5-(grade % 5)) < 3:
            if (grade % 5) == 0:
                print(grade)
            elif(5-(grade % 5)) == 1:
                print(grade+1)
            else:
                print(grade+2)
        else:
            print(grade)
    return


n = int(input())
for i in range(n):
    grade = int(input())
    rounder(grade)
