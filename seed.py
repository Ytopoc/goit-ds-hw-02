from faker import Faker
from connect import create_connect, infa 
from random import randint

NUMBER_USERS = 10
email_set = set()
fullname_set= set()
fake = Faker()

# Заповнення таблиці users
while len(email_set) != NUMBER_USERS:
    email_set.add(fake.email())

while len(fullname_set) != NUMBER_USERS:
    fullname_set.add(fake.name())

fullname_list= list(fullname_set)
email_list= list(email_set)
 
with create_connect(infa) as conn:
    cur = conn.cursor()
    count = 0
#Якщо Ви бажаєте зробити більше рядків - закоментуйте це
#####################################
    cur.execute("SELECT COUNT(*) FROM users")
    count = cur.fetchone()[0]
#####################################
    if count == 0:
            for i in range(NUMBER_USERS):
                fullname= fullname_list[i]
                email = email_list[i]
                cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))
            cur.close()
            conn.commit()


 


# Заповнення таблиці status
with create_connect(infa) as conn:
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM status")
    count = cur.fetchone()[0]
    if count == 0:
        statuses = ['new', 'in progress', 'completed']
        for status in statuses:
            cur.execute("INSERT INTO status (name) VALUES (%s)", (status,))
        conn.commit()
        cur.close()


#Заповнення таблиці tasks
task_1= ('Illegally smuggling watermelons across the Moldovan border.', 
'''Your task is to navigate the intricate web of Moldova\'s border
control as you attempt to smuggle watermelons across its borders. The stakes are high, and the border patrol is vigilant. 
Use your cunning and resourcefulness to outsmart the authorities and ensure the safe passage of the contraband fruit.
But remember, one wrong move could land you in serious trouble with the law.''')


task_2= ('Organize a protest because left-handed people are not provided with left-handed cups.', 
'''Take a stand for inclusivity and equality! 
Lead a protest demanding the production of cups specifically designed for left-handed individuals.
It's time to ensure that everyone, regardless of their dominant hand, can enjoy a comfortable and convenient drinking experience. ''')


task_3= ('To steal a wheelchair from someone during a wheelchair users\' half-marathon.', 
'''Challenge your moral compass as you 
embark on a daring mission to steal a wheelchair during a half-marathon for wheelchair users.
Navigate the ethical complexities as you confront the consequences of your actions, 
testing the limits of empathy and integrity in the face of temptation. ''')


task_4= ('To come to an orphanage posing as a child welfare agency and teach children to use swear words', 
'''Explore the blurred lines of morality as you infiltrate an 
orphanage under false pretenses, masquerading as a child welfare representative.
Your mission: to introduce profanity to innocent children. 
Navigate the delicate balance between deception and responsibility as you confront the ethical implications of your actions.''')


task_list= [task_1, task_2, task_3, task_4]

with create_connect(infa) as conn:
    cur = conn.cursor()
    count= 0 
#Якщо Ви бажаєте зробити більше рядків - закоментуйте це
#Але завдання будуть повторюватись, бо мені не вистачило уяви на більше
#####################################
    cur.execute("SELECT COUNT(*) FROM tasks")
    count = cur.fetchone()[0]
#####################################
    if count == 0:
                for i in task_list: 
                    task_tuple= i + (randint(1, 3), randint(1, 10))
                    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", task_tuple)
                cur.close()
                conn.commit()

        

