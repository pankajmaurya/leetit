import random
import sqlite3
import uuid

db_file = "./db/test_install.db"
timeout = 5000

connection = sqlite3.connect(db_file, timeout)
cur = connection.cursor()
cur.execute("create table test(id int, value text)")
connection.commit()

connection.close()

