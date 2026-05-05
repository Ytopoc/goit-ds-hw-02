import os
from contextlib import contextmanager

import psycopg2
from dotenv import load_dotenv

load_dotenv()

# [host, dbname, user, password, port] — read from environment.
infa = [
    os.getenv("POSTGRES_HOST", "localhost"),
    os.getenv("POSTGRES_DB", "postgres"),
    os.getenv("POSTGRES_USER", "postgres"),
    os.environ["POSTGRES_PASSWORD"],
    int(os.getenv("POSTGRES_PORT", "5432")),
]


@contextmanager
def create_connect(spisok):
    conn = psycopg2.connect(
        host=spisok[0],
        dbname=spisok[1],
        user=spisok[2],
        password=spisok[3],
        port=spisok[4],
    )
    yield conn
    conn.rollback()
    conn.close()
