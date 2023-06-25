import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from daabee import session
from create_basssee import Teacher, Student, TeacherStudent,Contact


fake = Faker('uk-UA')


def insert_students():
    for _ in range(10):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address()
        )
        session.add(student)


def insert_teachers():
    for _ in range(6):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            start_work=fake.date_between(start_date='-7y')
        )
        session.add(teacher)


def insert_rel():
    students = session.query(Student).all()
    teachers = session.query(Teacher).all()

    for student in students:
        rel = TeacherStudent(teacher_id=random.choice(teachers).id, student_id=student.id)
        session.add(rel)

def insert_contacts():
    students = session.query(Student).all()

    for _ in range(len(list(students)) + 7):
        contact = Contact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            student_id=random.choice(students).id
        )
        session.add(contact)

if __name__ == '__main__':
    try:
        insert_students()
        insert_teachers()
        insert_contacts()
        session.commit()
        insert_rel()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()