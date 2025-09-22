import sqlite3

# Connect to database (or create if it doesn’t exist)
conn = sqlite3.connect('sqlwork3.sqlite')
cur = conn.cursor()

# Drop table if it already exists
cur.execute('DROP TABLE IF EXISTS Counts')

# Create new table
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Open file
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fh = open(fname)

# Process each line
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]   # extract organization (domain)

    # Check if org exists in DB
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

# 🚀 Commit ONCE after the loop (much faster than committing every row)
conn.commit()

# Print top 10 results
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print("Top 10 organizations:")
for row in cur.execute(sqlstr):
    print(row[0], row[1])

cur.close()
