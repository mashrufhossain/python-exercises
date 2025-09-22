import urllib.request
import xml.etree.ElementTree as ET

# Prompt for URL
url = input('Enter location: ')
print('Retrieving', url)
# http://py4e-data.dr-chuck.net/comments_2059915.xml

# Read XML data from URL
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

# Parse XML
tree = ET.fromstring(data)

# Find all <count> elements
counts = tree.findall('.//count')

# Count and Sum
nums = [int(c.text) for c in counts]
print('Count:', len(nums))
print('Sum:', sum(nums))
