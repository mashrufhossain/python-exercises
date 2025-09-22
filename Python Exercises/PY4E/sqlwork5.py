# This application will read roster data in JSON format, parse the file, and then produce an SQLite database that contains a User, Course, 
# and Member table and populate the tables from the data file


import json
import sqlite3

# Connect to database
conn = sqlite3.connect('sqlwork5.sqlite')
cur = conn.cursor()

# Drop existing tables
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;
''')

# Create tables
cur.executescript('''
CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

# Load JSON file
fname = 'roster_data.json'
data = json.load(open(fname))

# Parse and insert
for entry in data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    # Insert User
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    # Insert Course
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    # Insert Member (with role!)
    cur.execute('''
        INSERT OR REPLACE INTO Member (user_id, course_id, role)
        VALUES (?, ?, ?)
    ''', (user_id, course_id, role))

# Commit and close
conn.commit()
print("✅ Database created: rosterdb.sqlite")

# Test query 1
print("\n--- Verification Query 1 ---")
for row in cur.execute('''
SELECT User.name, Course.title, Member.role
FROM User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2
'''):
    print(row)

# Test query 2 (the hex check)
print("\n--- Verification Query 2 ---")
cur.execute('''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X
FROM User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY X LIMIT 1
''')
print(cur.fetchone())


# Close connection
cur.close()
conn.close()