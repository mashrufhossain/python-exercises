import csv
import sqlite3

# Connect (or create) the database
conn = sqlite3.connect('sqlwork4.sqlite')
cur = conn.cursor()

# Drop tables if they exist
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
''')

# Create new normalized tables
cur.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Open the CSV file
fname = 'tracks.csv'
with open(fname) as f:
    reader = csv.reader(f)
    header = next(reader)  # skip header row
    for row in reader:
        if len(row) < 7:  # must have at least 7 fields
            continue

        # Map indexes based on YOUR tracks.csv
        title  = row[0]   # Track
        artist = row[1]   # Artist
        album  = row[2]   # Album
        rating = row[3]   # Rating
        count  = row[4]   # Play Count
        length = row[5]   # Time (len)
        genre  = row[6]   # Genre

        # Skip if required fields are missing
        if not title or not artist or not album or not genre:
            continue

        # Insert Artist
        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
        artist_id = cur.fetchone()[0]

        # Insert Genre
        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
        genre_id = cur.fetchone()[0]

        # Insert Album
        cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
        album_id = cur.fetchone()[0]

        # Insert Track
        cur.execute('''
            INSERT OR REPLACE INTO Track
            (title, album_id, genre_id, len, rating, count)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, album_id, genre_id, length, rating, count))

# Commit changes
conn.commit()
print("✅ Database created and populated successfully: sqlwork4.sqlite")

# Run the grading query
cur.execute('''
SELECT Track.title, Artist.name, Album.title, Genre.name 
FROM Track 
JOIN Genre 
JOIN Album 
JOIN Artist 
ON Track.genre_id = Genre.id 
   AND Track.album_id = Album.id 
   AND Album.artist_id = Artist.id
ORDER BY Artist.name, Track.title 
LIMIT 3
''')

# Print results neatly
print("\nTop 3 results:")
for row in cur.fetchall():
    print(row[0], row[1], row[2], row[3])

# Close connection
cur.close()
conn.close()
