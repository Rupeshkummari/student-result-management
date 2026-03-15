from results.models import Student, Subject, Result  # type: ignore
import random
from decimal import Decimal

# Subjects
subjects_data = [
    {'name': 'Data Structures', 'code': 'CS201'},
    {'name': 'Algorithms', 'code': 'CS202'},
    {'name': 'Database Systems', 'code': 'CS203'},
    {'name': 'Operating Systems', 'code': 'CS204'},
    {'name': 'Computer Networks', 'code': 'CS205'},
]
subjects = []
for sub in subjects_data:
    obj, created = Subject.objects.get_or_create(code=sub['code'], defaults={'name': sub['name']})
    subjects.append(obj)

# Students
students_data = [
    {'roll_no': '21CS101', 'name': 'Alice Smith', 'email': 'alice@example.com', 'gender': 'F', 'department': 'Computer Science', 'batch': '2021-2025'},
    {'roll_no': '21CS102', 'name': 'Bob Johnson', 'email': 'bob@example.com', 'gender': 'M', 'department': 'Computer Science', 'batch': '2021-2025'},
    {'roll_no': '21IT201', 'name': 'Charlie Brown', 'email': 'charlie@example.com', 'gender': 'M', 'department': 'Information Technology', 'batch': '2021-2025'},
    {'roll_no': '21ME301', 'name': 'Diana Prince', 'email': 'diana@example.com', 'gender': 'F', 'department': 'Mechanical Engineering', 'batch': '2021-2025'},
    {'roll_no': '21CV401', 'name': 'Ethan Hunt', 'email': 'ethan@example.com', 'gender': 'M', 'department': 'Civil Engineering', 'batch': '2021-2025'},
]
students = []
for stu in students_data:
    obj, created = Student.objects.get_or_create(roll_no=stu['roll_no'], defaults=stu)
    students.append(obj)

# Results
grades = ['O', 'A+', 'A', 'B+', 'B', 'C', 'F']
for student in students:
    sampled_subjects = random.sample(subjects, 3)
    for subject in sampled_subjects:
        marks_float = random.uniform(40.0, 95.0)
        marks = float(f"{marks_float:.2f}")
        if marks >= 90: grade = 'O'
        elif marks >= 80: grade = 'A+'
        elif marks >= 70: grade = 'A'
        elif marks >= 60: grade = 'B+'
        elif marks >= 50: grade = 'B'
        elif marks >= 45: grade = 'C'
        else: grade = 'F'
        Result.objects.get_or_create(
            student=student, 
            subject=subject, 
            semester=1, 
            exam_year=2025, 
            defaults={'marks': Decimal(str(marks)), 'grade': grade}
        )
