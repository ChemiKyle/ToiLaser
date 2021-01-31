'''Used https://www.cockroachlabs.com/docs/v20.2/build-a-python-app-with-cockroachdb for info'''

import psycopg2

DATABASE = 'toilaser'
PORT = 41335
HOST = 'localhost'
USER = 'db_user'
PASSWORD = 'password'


def create_table(conn):
    '''Creates logging table if not already present'''
    with conn.cursor() as c:
        c.execute("CREATE TABLE IF NOT EXISTS log (id SERIAL PRIMARY KEY, timestamp TIMESTAMPTZ, location_id INT)")
    conn.commit()


def add_timestamp(conn, location_id):
    '''Adds timestamp'''
    sql = '''INSERT INTO log (timestamp, location_id) VALUES ('now', %i)'''
    with conn.cursor() as c:
        c.execute(sql % (location_id))
    conn.commit()


def create_connection():
    '''Connects to database'''
    conn = psycopg2.connect(
        database=DATABASE,
        port=PORT,
        host=HOST,
        user=USER,
        password=PASSWORD)
    with conn.cursor() as c:
        c.execute("use toilaser")
    return conn