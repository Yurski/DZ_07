from sqlalchemy import func
from db import Student, Grade, Subject, Group, Teacher, session


def select_1():
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                    .join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()
    return result

def select_2(subject_name):
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                    .join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Student.id)\
                    .order_by(func.avg(Grade.grade).desc()).first()
    return result

def select_3(subject_name):
    result = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                    .join(Student).join(Grade, Grade.student_id == Student.id)\
                    .join(Subject, Subject.id == Grade.subject_id)\
                    .filter(Subject.name == subject_name)\
                    .group_by(Group.id).all()
    return result


def select_4():
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).first()[0]
    return result

def select_5(teacher_name):
    result = session.query(Subject.name).join(Teacher).filter(Teacher.fullname == teacher_name).all()
    return result

def select_6(group_name):
    result = session.query(Student.fullname).join(Group).filter(Group.name == group_name).all()
    return result

def select_7(group_name, subject_name):
    result = session.query(Student.fullname, Grade.grade).join(Group).join(Grade).join(Subject)\
                    .filter(Group.name == group_name, Subject.name == subject_name).all()
    return result

def select_8(teacher_name):
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                    .join(Subject).join(Teacher).filter(Teacher.fullname == teacher_name).first()[0]
    return result

def select_9(student_name):
    result = session.query(Subject.name).join(Grade).join(Student).filter(Student.fullname == student_name).all()
    return result

def select_10(student_name, teacher_name):
    result = session.query(Subject.name).join(Grade).join(Student).join(Teacher)\
                    .filter(Student.fullname == student_name, Teacher.fullname == teacher_name).all()
    return result

if __name__ == "__main__":
    print("Top 5 students with highest average grades:")
    print(select_1())
    print("\nStudent with highest average grade in a specific subject:")
    print(select_2())
    print("\nAverage grade for groups in a specific subject:")
    print(select_3())
    print("\nAverage grade across all subjects:")
    print(select_4())
    print("\nCourses taught by a specific teacher:")
    print(select_5())
    print("\nList of students in a specific group:")
    print(select_6())
    print("\nGrades of students in a specific group for a specific subject:")
    print(select_7())
    print("\nAverage grade given by a specific teacher across their subjects:")
    print(select_8())
    print("\nCourses attended by a specific student:")
    print(select_9())
    print("\nCourses taught to a specific student by a specific teacher:")
    print(select_10())

