#!/bin/python3

# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grade):
            if grade < 38:
                round_grades.append(grade)            # failing grade detected and written in list
            elif grade >= 38 and (5 - (grade % 5)) < 3:
                grade += (5 - (grade % 5)) # round up to the next multiple of 5 by addition the remainder
                round_grades.append(grade)
            elif grade >= 38 and (5 - (grade % 5)) >= 3:
                round_grades.append(grade)            

grades_count = int(input().strip())
grades = []
round_grades = []

for i in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)
    result = gradingStudents(grades[i]) # iterate through expanding list and apply function to each new element in the list
    if result: # check if function call returns None and not append it to the list
        round_grades.append(result)

# round_grades = filter(None, round_grades)

print('grade list:', grades)
print('grade list after rounding:',round_grades)


