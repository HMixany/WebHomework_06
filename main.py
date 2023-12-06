import logging
from contextlib import contextmanager

import psycopg2
from psycopg2 import DatabaseError

from insert import insert_data

HOST_DB = 'localhost'
NAME_DB = 'test'
USER_DB = 'postgres'
PASSWORD_DB = '321456'


@contextmanager
def create_connection():
    try:
        """ create a database connection to database """
        conn = psycopg2.connect(host=HOST_DB, database=NAME_DB, user=USER_DB, password=PASSWORD_DB)
        yield conn
        conn.close()
    except psycopg2.OperationalError as err:
        raise RuntimeError(f'Failed to create database connection {err}')


def create_table(conn, sql_expression: str):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :return:
    """
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


def select_data(conn, sql_expression: str):
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        result = c.fetchall()
        return result
    except DatabaseError as e:
        logging.error(e)
    finally:
        c.close()


if __name__ == '__main__':
    with open('create_tables.sql', 'r') as file:
        sql_create_tables = file.read()

    try:
        with create_connection() as conn:
            if conn is not None:
                # create tables
                create_table(conn, sql_create_tables)
                # заповнюємо таблиці
                insert_data(conn)
                # робимо 10 запитів
                for i in range(1, 11):
                    with open(f'query_{i}.sql', 'r') as file:
                        sql_expression = file.read()
                    print(select_data(conn, sql_expression))
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)


