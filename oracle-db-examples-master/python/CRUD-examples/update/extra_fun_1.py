# Code Sample from the tutorial at https://learncodeshare.net/2015/07/02/update-crud-using-cx_oracle/
#  section titled "Extra Fun 1"
# Using the base template, the example code executes a simple update using positional bind variables.

import cx_Oracle
import os
connectString = os.getenv('DB_CONNECT') # The environment variable for the connect string: DB_CONNECT=user/password@database
con = cx_Oracle.connect(connectString)

def get_all_rows(label, data_type='people'):
 # Query all rows
 cur = con.cursor()
 if (data_type == 'pets'):
    statement = 'select id, name, owner, type from lcs_pets order by owner, id'
 else:
    statement = 'select id, name, age, notes from lcs_people order by id'
 cur.execute(statement)
 res = cur.fetchall()
 print(label + ': ')
 print (res)
 print(' ')
 cur.close()

get_all_rows('Original Data')

cur = con.cursor()
statement = 'update lcs_people set notes = :1 where id = :2'
cur.execute(statement, ("I like cats", 1))
con.commit()

get_all_rows('New Data')
