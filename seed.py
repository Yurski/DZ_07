from faker import Faker
from random import randint, choice
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Student, Group, Teacher, Subject, Grade
from datetime import datetime, timedelta

fake = Faker()

# DB_URL = "postgresql://postgres:12345@localhost/postgres"
DB_URL = "sqlite:///school.db" 
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

def create_students(num_students):
    for _ in range(num_students):
        student = Student(fullname=fake.name())
        session.add(student)

def create_groups(num_groups):
    for i in range(num_groups):
        group = Group(name=f'Group {i+1}')
        session.add(group)

def create_teachers(num_teachers):
    for _ in range(num_teachers):
        teacher = Teacher(fullname=fake.name())
        session.add(teacher)

def create_subjects(num_subjects):
    teachers = session.query(Teacher).all()
    for _ in range(num_subjects):
        teacher = choice(teachers)
        subject = Subject(name=fake.word(), teacher=teacher)
        session.add(subject)

def create_grades(num_grades):
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for _ in range(num_grades):
        student = choice(students)
        subject = choice(subjects)
        grade_value = randint(1, 10)
        date_received = fake.date_time_between(start_date='-1y', end_date='now')
        grade_entry = Grade(student_id=student.id, subject_id=subject.id, grade=grade_value, date_received=date_received)
        session.add(grade_entry)

if __name__ == '__main__':
    create_students(50)
    create_groups(3)
    create_teachers(5)
    create_subjects(8)
    create_grades(20)

    session.commit()
