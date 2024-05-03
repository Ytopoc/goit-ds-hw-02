import psycopg2
from contextlib import contextmanager

#!!!!!!!!
#!!!!!!!!
#!!!!!!!!
infa= ["localhost", "postgres", "postgres", "228402", 5432] #   [host, dbname, user, password, port]
#!!!!!!!!
#!!!!!!!!
#!!!!!!!!

@contextmanager
def create_connect(spisok):
    conn= psycopg2.connect(host=spisok[0],dbname=spisok[1],user=spisok[2],password=spisok[3], port=spisok[4])
    yield conn
    conn.rollback()
    conn.close()


