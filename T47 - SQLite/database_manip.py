import sqlite3
db = sqlite3.connect('python_programming_db')
cursor = db.cursor()  # Get a cursor object

cursor.execute('''
    DROP TABLE IF EXISTS Student;
''')

cursor.execute('''  
    CREATE TABLE IF NOT EXISTS Student
    (
        id INTEGER PRIMARY KEY, 
        name TEXT,
        grade INTEGER
    );
''')
db.commit()

# Inserting students
cursor.execute('''
    INSERT INTO Student
    (
        id,
        name, 
        grade
    )
    VALUES
    (
        55,
        'Carl Davis',
        61
    ),
    (
        66,
        'Dennis Fredrickson',
        88
    ),
    (
        77,
        'Jane Richards',
        78
    ),
    (
        12,
        'Peyton Sawyer',
        45
    ),
    (
        2,
        'Lucas Brooke',
        99
    )
    ''')
db.commit()

# Print all records in Student
cursor.execute('''
   SELECT * FROM Student;
    ''')
query_student = cursor.fetchall()
print(query_student)

# Select all records with grade between 60 and 80
cursor.execute('''
    SELECT * FROM Student
    WHERE
    grade BETWEEN 60 AND 80;
    ''')
query_student = cursor.fetchall()
print(query_student)

# Update Carl Davis' grade to 65
cursor.execute('''
    UPDATE Student
    SET grade = 65
    WHERE
    name = 'Carl Davis';
    ''')
db.commit()

# Print all records in Student
cursor.execute('''
   SELECT * FROM Student;
    ''')
query_student = cursor.fetchall()
print(query_student)

# Delete Dennis Fredrickson's row
cursor.execute('''
    DELETE FROM Student
    WHERE
    name = 'Dennis Fredrickson'
''')

# Print all records in Student
cursor.execute('''
   SELECT * FROM Student;
    ''')
query_student = cursor.fetchall()
print(query_student)

# Change the grade of all people with an id less than 55
cursor.execute('''
    UPDATE Student
    SET grade = 1
    WHERE
    id < 55;
    ''')
db.commit()

# Print all records in Student
cursor.execute('''
   SELECT * FROM Student;
    ''')
query_student = cursor.fetchall()
print(query_student)

db.close()
print('Connection to database closed')
