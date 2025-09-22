import urllib.request
import json

# Prompt for URL
# http://py4e-data.dr-chuck.net/comments_2059916.json
url = input('Enter location: ')
print('Retrieving', url)

# Read data from URL
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

# Parse JSON
info = json.loads(data)

# Extract counts
counts = [item['count'] for item in info['comments']]

# Count and Sum
print('Count:', len(counts))
print('Sum:', sum(counts))
