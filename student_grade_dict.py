student_grades = {
    'Student1': 'B',
    'Student2': 'C',
    'Student3': 'A',
    'Student4': 'B+',
    'Student5': 'A-'
}

print("Entire dictionary:", student_grades)

print("Grade of third student:", student_grades['Student3'])

student_grades['Student2'] = 'A'

del student_grades['Student5']

last_key = list(student_grades.keys())[-1]
last_value = student_grades[last_key]
print("Last key-value pair:", last_key, last_value)