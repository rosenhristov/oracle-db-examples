# Code Sample from the tutorial at https://learncodeshare.net/2015/06/26/insert-crud-using-cx_oracle/
#  section titled "Insert more than 1 row"
# Using the base template, the example code executes a simple insert using positional bind variables.
#  Using the executemany function an array of data is inserted into the table.

import cx_Oracle
import os
connectString = os.getenv('DB_CONNECT') # The environment variable for the connect string: DB_CONNECT=user/password@database
con = cx_Oracle.connect(connectString)

def get_all_rows(label):
 # Query all rows
 cur = con.cursor()
 statement = 'select id, name, age, notes from lcs_people order by id'
 cur.execute(statement)
 res = cur.fetchall()
 print(label + ': ')
 print (res)
 print(' ')
 cur.close()

get_all_rows('Original Data')

rows = [{'name':'Sandy', 'age':31, 'notes':'I like horses'}, {'name':'Suzy', 'age':29, 'notes':'I like rabbits'}]
cur = con.cursor()
cur.bindarraysize = 2
statement = 'insert into lcs_people(name, age, notes) values (:name, :age, :notes)'
cur.executemany(statement, rows)
con.commit()

get_all_rows('New Data')
