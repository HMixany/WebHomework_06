import logging
from random import randint

from faker import Faker
from psycopg2 import DatabaseError


fake = Faker('uk-Ua')


def insert_data(conn):
    cur = conn.cursor()
    try:
        # Додавання груп
        for _ in range(3):
            cur.execute('INSERT INTO groups (name) VALUES (%s)', (fake.word(),))

        # Додавання викладачів
        for _ in range(3):
            cur.execute('INSERT INTO teachers (full_name) VALUES (%s)', (fake.name(),))

        # Додавання предметів із вказівкою викладача
        for teacher_id in range(1, 4):
            for _ in range(2):
                cur.execute('INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)', (fake.word(), teacher_id))

        # додавання студентів і оцінок
        for group_id in range(1, 4):
            for _ in range(15):
                cur.execute('INSERT INTO students (full_name, group_id) VALUES (%s, %s) RETURNING id',
                            (fake.name(), group_id))
                student_id = cur.fetchone()[0]
                for subject_id in range(1, 7):
                    for _ in range(3):
                        cur.execute(
                            'INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (%s, %s, %s, %s)',
                            (student_id, subject_id, randint(0, 100), fake.date_this_decade()))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        cur.close()

