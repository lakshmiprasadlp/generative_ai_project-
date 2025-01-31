import sqlite3


conn = sqlite3.connect('students.db')



cuser=conn.cursor()


table="""

create TABLE students (name varchar(255),Class varchar(255),marks int);
"""


cuser.execute(table)

cuser.execute("INSERT INTO students VALUES ('John Doe', 'Class 10', 90)")
cuser.execute("INSERT INTO students VALUES ('Vignesh', 'Class 10', 85)")
cuser.execute("INSERT INTO students VALUES ('visnu', 'Class 10', 60)")
cuser.execute("INSERT INTO students VALUES (' deakeshit ', 'Class 10', 68)")
cuser.execute("INSERT INTO students VALUES (' adharesh', 'Class 10', 72)")
cuser.execute("INSERT INTO students VALUES ('heamenth', 'Class 10', 68)")
cuser.execute("INSERT INTO students VALUES ('venkat ', 'Class 10', 77)")

cuser.execute("INSERT INTO students VALUES ('kiran', 'Class 11', 99)")
cuser.execute("INSERT INTO students VALUES ('manu', 'Class 11', 80)")
cuser.execute("INSERT INTO students VALUES ('kp frind', 'Class 11', 85)")
cuser.execute("INSERT INTO students VALUES ('vivak', 'Class 11', 59)")
cuser.execute("INSERT INTO students VALUES ('Adhi', 'Class 11', 95)")

cuser.execute("INSERT INTO students VALUES ('Reaventh', 'Class 12', 90)")
cuser.execute("INSERT INTO students VALUES ('sumant', 'Class 12', 85)")
cuser.execute("INSERT INTO students VALUES ('varun', 'Class 12', 70)")
cuser.execute("INSERT INTO students VALUES ('chirag', 'Class 12', 79)")
cuser.execute("INSERT INTO students VALUES ('vinai', 'Class 12', 68)")

print("Table created successfully")

data=cuser.execute("SELECT * FROM students")

for i in data:
    print(i)
    
conn.commit()
conn.close()