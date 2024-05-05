import sqlite3
import faker
from random import randint, choice

database = './db_test.sqlite'
script = './Script_createTables.sql'

def create_db():
    with open(script, 'r') as f:
        sql = f.read()

    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.executescript(sql)

NUMBER_USERS = 3
NUMBER_TASKS = 5
NUMBER_STATUSES = 3
STATUSES = ["new", "in progress", "completed"]

def generate_fake_data() -> tuple():
    fake_users = []
    fake_emails = []
    fake_tasks = []
    fake_descriptions = []
    
    fake_data = faker.Faker()

# generate users and their emails 
    for _ in range(NUMBER_USERS):
        fake_users.append(fake_data.name())
        fake_emails.append(fake_data.email())

# generate tasks' names and descriptions
    for _ in range(NUMBER_TASKS):
        fake_tasks.append(fake_data.text(100))
        fake_descriptions.append(fake_data.text())

    return fake_users, fake_emails, fake_tasks, fake_descriptions

def prepare_data(status_raw, users_raw, emails_raw, tasks_raw, description_raw):
    prepared_status = []
    prepared_users = []
    prepared_tasks = []

    for status in status_raw:
        prepared_status.append((status, ))

    for i in range(NUMBER_USERS):
        prepared_users.append((users_raw[i], emails_raw[i]))

    for i in range(NUMBER_TASKS):
        prepared_tasks.append((tasks_raw[i], description_raw[i], randint(1, NUMBER_STATUSES), randint(1, NUMBER_USERS)))    
    
    return prepared_status, prepared_users, prepared_tasks

def insert_data_to_db(prepared_status, prepared_users, prepared_tasks):
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        sql_to_status = """ INSERT INTO status(name) VALUES(?)"""
        cur.executemany(sql_to_status, prepared_status)

        sql_to_users = """ INSERT INTO users(fullname, email) VALUES(?,?)"""
        cur.executemany(sql_to_users, prepared_users)

        sql_to_tasks = """ INSERT INTO tasks(title, description, status_id, user_id) VALUES(?,?,?,?)"""
        cur.executemany(sql_to_tasks, prepared_tasks)


if __name__ == "__main__":
    create_db()
    statuses, users, tasks = prepare_data(STATUSES, *generate_fake_data())
    insert_data_to_db(statuses, users, tasks)





