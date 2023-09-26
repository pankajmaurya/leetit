import random
import sqlite3
import uuid

db_file = "./db/test_install.db"
timeout = 5000

connection = sqlite3.connect(db_file, timeout)
cur = connection.cursor()
res = cur.execute("select * from test").fetchall()
print(res)

print("Inserting another row...")
id = random.randint(1, 100)
val = str(uuid.uuid4())

command = "insert into test values ({}, '{}')".format(id, val)
cur.execute(command)
connection.commit()

connection.close()

