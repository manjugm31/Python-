student_marks = {
    'John': 85,
    'Alice': 90,
    'Bob': 75,
    'Emily': 88,
    'David': 82,
    'Linda': 95,
    'Michael': 78,
    'Sophia': 92,
    'Daniel': 87,
    'Olivia': 80
}
grade={}
for Student in student_marks:
    i=student_marks[Student]
    if i>=90:
        grade[Student]="A+"
    elif i>=90 and i<=80:
         grade[Student]="A"
    elif i>=80 and i<=70:
        grade[Student]="B+"
    elif i>=70 and i<=50:
        grade[Student]="B"
    elif i>=50 and i<=35:
        grade[Student]="c+"
    else:
         grade[Student]="fail"
print(grade)
    