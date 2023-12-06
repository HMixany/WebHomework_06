import logging

from psycopg2 import DatabaseError


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
