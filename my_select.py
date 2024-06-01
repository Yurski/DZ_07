from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from app.models import Student, Group, Teacher, Subject, Grade

def select_1(session):
    result = session.query(Student.fullname, func.avg(Grade.grade).label('average_grade')) \
                    .join(Grade) \
                    .group_by(Student.id) \
                    .order_by(func.avg(Grade.grade).desc()) \
                    .limit(5) \
                    .all()
    return result

def select_2(session, subject_name):
    result = session.query(Student.fullname, func.avg(Grade.grade).label('average_grade')) \
                    .join(Grade) \
                    .join(Subject) \
                    .filter(Subject.name == subject_name) \
                    .group_by(Student.id) \
                    .order_by(func.avg(Grade.grade).desc()) \
                    .first()
    return result

def select_3(session, subject_name):
    result = session.query(Group.name, func.avg(Grade.grade).label('average_grade')) \
                    .join(Student, Student.group_id == Group.id) \
                    .join(Grade) \
                    .join(Subject) \
                    .filter(Subject.name == subject_name) \
                    .group_by(Group.id) \
                    .all()
    return result

def select_4(session):
    result = session.query(func.avg(Grade.grade).label('average_grade')).scalar()
    return result

def select_5(session, teacher_name):
    result = session.query(Subject.name).join(Teacher).filter(Teacher.fullname == teacher_name).all()
    return result

def select_6(session, group_name):
    result = session.query(Student.fullname).join(Group).filter(Group.name == group_name).all()
    return result

def select_7(session, group_name, subject_name):
    result = session.query(Student.fullname, Grade.grade) \
                    .join(Group) \
                    .join(Grade) \
                    .join(Subject) \
                    .filter(Group.name == group_name) \
                    .filter(Subject.name == subject_name) \
                    .all()
    return result

def select_8(session, teacher_name):
    result = session.query(func.avg(Grade.grade).label('average_grade')) \
                    .join(Subject) \
                    .join(Teacher) \
                    .filter(Teacher.fullname == teacher_name) \
                    .scalar()
    return result

def select_9(session, student_name):
    result = session.query(Subject.name) \
                    .join(Grade) \
                    .join(Student) \
                    .filter(Student.fullname == student_name) \
                    .all()
    return result

def select_10(session, student_name, teacher_name):
    result = session.query(Subject.name) \
                    .join(Teacher) \
                    .filter(Subject.teacher.has(fullname=teacher_name)) \
                    .join(Grade) \
                    .join(Student) \
                    .filter(Student.fullname == student_name) \
                    .all()
    return result

if __name__ == "__main__":
    # Створення з'єднання з базою даних
    DB_URL = "sqlite:///school.db" 
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Виклик функції select_1
    result = select_1(session)
    print("5 студентів із найбільшим середнім балом з всіх предметів:", result)

    # Виклик функції select_2
    result = select_2(session, "card")
    print("Студент із найвищим середнім балом з певного предмета card:", result)

    # Виклик функції select_3
    result = select_3(session, "important")
    print("Середній бал в групах з певного предмета:", result)

    # Виклик функції select_4
    result = select_4(session)
    print("Середній бал на потоці:", result)

    # Виклик функції select_5
    result = select_5(session, "Anna Watson")
    print("Курси читає певний викладач Anna Watson:", result)

    # Виклик функції select_6
    result = select_6(session, "Group 1")
    print("Список студентів в певній групі Group 1:", result)

    # Виклик функції select_7
    result = select_7(session, "Group 2", "each")
    print("Оцінки студентів в окремій групі Group 2 з певного предмета each:", result)

    # Виклик функції select_8
    result = select_8(session, "Gabriela Fernandez")
    print("Середній бал, який ставить певний викладач зі своїх предметів Gabriela Fernandez:", result)

    # ПВиклик функції select_9
    result = select_9(session, "Stacey Patrick")
    print("Список курсів, які відвідує певний студент Stacey Patrick:", result)

    # Виклик функції select_10
    result = select_10(session, "Deborah Shaffer", "Katie Winters")
    print("Список курсів, які певному студенту Deborah Shaffer читає певний викладач Katie Winters:", result)








