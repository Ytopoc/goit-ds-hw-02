from connect import create_connect, infa
#Видаляє всі таблиці з БД
with create_connect(infa) as conn:
    cur = conn.cursor()
    cur.execute('DROP TABLE users CASCADE')
    cur.execute('DROP TABLE status CASCADE')
    cur.execute('DROP TABLE tasks CASCADE')
    cur.close()
    conn.commit()
