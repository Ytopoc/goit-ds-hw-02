from psycopg2 import Error
from connect import create_connect, infa
try:
    with create_connect(infa) as conn:

        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100) NOT NULL ,
        email VARCHAR(100) UNIQUE NOT NULL
        )""")

        cur.execute("""CREATE TABLE IF NOT EXISTS status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL
        )""")

        cur.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100),
        description TEXT,
        status_id INTEGER REFERENCES status (id) ON DELETE CASCADE ON UPDATE CASCADE,
        user_id INTEGER REFERENCES users (id) ON DELETE CASCADE  ON UPDATE CASCADE 
        )
        """)
        conn.commit()
except Error as e:
    print(e)

     

