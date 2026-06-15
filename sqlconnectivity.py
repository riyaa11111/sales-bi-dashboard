from tkinter.constants import BROWSE

import pymysql

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '12345678',
    database = 'city'
)

print("connection successful")

cursor = conn.cursor()
cursor.execute("show tables")
for table in cursor:
    print(table)

cursor.execute(f"select * from {'student'}")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
