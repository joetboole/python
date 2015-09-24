#!/usr/bin/python
import sqlite3

con = sqlite3.connect("C:/Users/dell/Desktop/db/shine-db")
cur = con.cursor()
# cur.execute('CREATE TABLE foo (o_id INTEGER PRIMARY KEY, fruit VARCHAR(20), veges VARCHAR(30))')
# con.commit()
# cur.execute('INSERT INTO foo (o_id, fruit, veges) VALUES(NULL, "apple", "broccoli")')
# con.commit()
# print (cur.lastrowid)

cur.execute('SELECT * FROM CYCLE')
print (cur.fetchall())
cur.execute('INSERT INTO CYCLE (START_DATE, END_DATE, MEMBER_ID, CYCLE_LENGTH, PERIOD_LENGTH) VALUES(NULL, "apple", "broccoli")')

print (cur.fetchall())