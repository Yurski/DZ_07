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

# def select_3(subject_name):
#     result = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
#                     .join(Student).join(Grade, Grade.student_id == Student.id)\
#                     .join(Subject, Subject.id == Grade.subject_id)\
#                     .filter(Subject.name == subject_name)\
#                     .group_by(Group.id).all()
#     return result

# def select_3(subject_name):
#     query = (
#         session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))
#         .join(Grade, Group.id == Grade.group_id)
#         .join(Subject, Subject.id == Grade.subject_id)
#         .filter(Subject.name == subject_name)
#         .group_by(Group.id)
#         .all()
#     )
#     return query

# def select_3(subject_name):
#     query = (
#         session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))
#         .join(Student, Group.id == Student.group_id)
#         .join(Grade, Student.id == Grade.student_id)
#         .join(Subject, Subject.id == Grade.subject_id)
#         .filter(Subject.name == subject_name)
#         .group_by(Group.id)
#         .all()
#     )
#     return query

# def select_3(subject_name):
#     query = (
#         session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))
#         .join(Group.students)
#         .join(Student.grades)
#         .join(Grade.subject)
#         .filter(Subject.name == subject_name)
#         .group_by(Group.id)
#         .all()
#     )
#     return query

# def select_3(subject_name):
#     query = (
#         session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))
#         .join(Group.students)
#         .join(Student.grades)
#         .join(Grade.subject)
#         .filter(Subject.name == subject_name)
#         .group_by(Group.id)
#         .all()
#     )
#     return query

# def select_3(subject_name):
#     query = (
#         session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))
#         .join(Grade)
#         .join(Subject)
#         .join(Group)  # Додаємо посилання на Group через Grade
#         .filter(Subject.name == subject_name)
#         .group_by(Student.fullname)
#         .all()
#     )
#     return query

def select_3(subject_name):
    query = (
        session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))
        .select_from(Group)
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .join(Subject, Subject.id == Grade.subject_id)
        .filter(Subject.name == subject_name)
        .group_by(Group.name)
        .all()
    )
    return query



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
    print("5 студентів із найбільшим середнім балом з всіх предметів:")
    print(select_1())
    print("Студент із найвищим середнім балом з певного предмета:")
    print(select_2("Math"))
    print("Середній бал в групах з певного предмета:")
    print(select_3("Physics"))
    print("Середній бал на потоці:")
    print(select_4())
    print("Курси читає певний викладач:")
    print(select_5("John Doe"))
    print("Список студентів в певній групі:")
    print(select_6("Group 1"))
    print("Оцінки студентів в окремій групі з певного предмета:")
    print(select_7("Group 2", "Chemistry"))
    print("Середній бал, який ставить певний викладач зі своїх предметів:")
    print(select_8("Jane Smith"))
    print("Список курсів, які відвідує певний студент:")
    print(select_9("Alice Johnson"))
    print("Список курсів, які певному студенту читає певний викладач:")
    print(select_10("Bob Brown", "Jane Smith"))

