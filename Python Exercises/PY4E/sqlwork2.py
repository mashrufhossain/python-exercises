import sqlite3

# Connect to database
conn = sqlite3.connect('sqlwork2.sqlite')
cur = conn.cursor()

# Drop and recreate table
cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('''
CREATE TABLE Ages (
    name VARCHAR(128),
    age INTEGER
)
''')

# Insert rows
cur.execute("INSERT INTO Ages (name, age) VALUES (?, ?)", ('Rebekkah', 21))
cur.execute("INSERT INTO Ages (name, age) VALUES (?, ?)", ('Launi', 19))
cur.execute("INSERT INTO Ages (name, age) VALUES (?, ?)", ('Zena', 28))
cur.execute("INSERT INTO Ages (name, age) VALUES (?, ?)", ('Phoenix', 28))
cur.execute("INSERT INTO Ages (name, age) VALUES (?, ?)", ('Todd', 13))
cur.execute("INSERT INTO Ages (name, age) VALUES (?, ?)", ('Amos', 35))

# Select both normal and hex
cur.execute("SELECT name || age AS original, hex(name || age) AS X FROM Ages ORDER BY X")

for row in cur:
    print(f"Original: {row[0]}  |  Hex: {row[1]}")

conn.commit()
cur.close()
conn.close()
