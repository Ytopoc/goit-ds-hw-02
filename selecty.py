from connect import create_connect, infa
from faker import Faker

fake = Faker()
# Отримати всі завдання певного користувача.
def select_tasks(conn):
    rows = None
    cur = conn.cursor()
    cur.execute("SELECT title, description FROM tasks WHERE user_id = 6;")
    rows = cur.fetchall()
    cur.close()
    return rows

# Вибрати завдання за певним статусом.
def select_status(conn):
    rows = None
    cur = conn.cursor()
    cur.execute("SELECT title, description FROM tasks WHERE status_id IN (SELECT id FROM status WHERE name = 'new') ")
    rows = cur.fetchall()
    cur.close()
    return rows

# Оновити статус конкретного завдання.
def update_status(conn):
     cur= conn.cursor()
     cur.execute("UPDATE tasks SET status_id = 1 WHERE id = 1 ")
     conn.commit()
     cur.close()    
     return 'Status updateted' 


# Отримати список користувачів, які не мають жодного завдання.
def unemployed(conn):
    rows = None
    cur = conn.cursor()
    cur.execute("SELECT fullname FROM users WHERE id NOT IN(SELECT user_id FROM tasks) ")
    rows = cur.fetchall()
    cur.close()
    return rows
     
# Додати нове завдання для конкретного користувача.
NewTask= ('Dig up your neighbor\'s apricot tree at night and plant a cactus in its place.',
'''Embark on a surreptitious mission under the cloak of 
darkness as you uproot your neighbor's beloved
apricot tree and replace it with a prickly cactus.
Navigate the ethical quandaries of property rights
and horticultural sabotage as you execute this audacious act of greenery subversion. 
Will your nocturnal escapade blossom into mischief or wilt under the weight of consequence?''', 1 )


def new_task(conn):
    rows = None
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE fullname = 'Anthony Wang'")
    rows = cur.fetchall()
    task_tuple = NewTask + rows[0]
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s) ", task_tuple )
    cur.close()
    conn.commit()
    return 'Task added '

# Отримати всі завдання, які ще не завершено.
def select_nocomplited_task(conn):
    rows = None
    cur = conn.cursor()
    cur.execute("SELECT title, description FROM tasks WHERE status_id IN (1, 2) ")
    rows = cur.fetchall()
    cur.close()
    return rows 

# Видалити конкретне завдання.
def delete_by_id(conn):
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = 1")
    cur.close()
    conn.commit()
    return "Task deleted"

# Знайти користувачів з певною електронною поштою.
def select_email(conn):
    rows = None
    cur = conn.cursor()
    cur.execute("SELECT fullname FROM users WHERE email LIKE '%.org' ")
    rows = cur.fetchall()
    cur.close()
    return rows 
     
# Оновити ім'я користувача.
def update_name(conn):
    names = None
    cur= conn.cursor()
    cur.execute("SELECT fullname FROM users ")
    names = cur.fetchall()
    while True:
        new_name= tuple()
        new_name=(fake.name() ,)
        if new_name not in names:
            break
    cur.execute("UPDATE users SET fullname = %s WHERE id = 10 ", new_name)
    conn.commit()
    cur.close()    
    return "Name updated"      

# Отримати кількість завдань для кожного статусу.
def tasks_by_status(conn):
    rows = None
    cur= conn.cursor()
    cur.execute("SELECT COUNT(title) as total_tasks, status_id FROM tasks GROUP BY status_id ")
    rows= cur.fetchall()
    cur.close()
    return rows 

# Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
def select_tasks_by_email(conn):
    rows = None
    cur = conn.cursor()
    cur.execute("SELECT t.id, t.title, t.description FROM tasks AS t JOIN users AS u ON u.id = t.user_id WHERE u.email LIKE '%@example.org'")
    rows = cur.fetchall()
    cur.close()
    return rows

# Отримати список завдань, що не мають опису.
#У мене всі завдання з описом...

def select_empty_description(conn):
    rows = None
    cur = conn.cursor()
    cur.execute("SELECT title FROM tasks WHERE description IS NULL")
    rows = cur.fetchall()
    cur.close()
    return rows


# Вибрати користувачів та їхні завдання, які є у статусі
def select_task_name(conn):
    rows = None
    cur = conn.cursor()
    cur.execute("SELECT users.fullname AS name, tasks.title AS task FROM tasks INNER JOIN users ON tasks.user_id = users.id WHERE tasks.status_id = 2")
    rows = cur.fetchall()
    cur.close()
    return rows


# Отримати користувачів та кількість їхніх завдань.
def select_users_tasks(conn):
    rows = None
    cur = conn.cursor()
    cur.execute("SELECT users.fullname AS name, COUNT(tasks.id) AS task_count FROM users LEFT JOIN tasks ON users.id = tasks.user_id GROUP BY users.id, users.fullname")
    rows = cur.fetchall()
    cur.close()
    return rows


if __name__ == "__main__":
    with create_connect(infa) as conn:
            print(select_users_tasks(conn))
