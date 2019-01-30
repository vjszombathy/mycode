#!/usr/bin/env python3
message = 'The letter grade is: '
print('What is your numeric grade? ')
numeric_grade = float(input())
if numeric_grade >= 90:
    message = message + 'A'
elif numeric_grade >= 80:
    message = message + 'B'
elif numeric_grade >= 70:
    message = message + 'C'
elif numeric_grade >= 60:
    message = message + 'D'
else:
    message = message + 'F'
print(message)
