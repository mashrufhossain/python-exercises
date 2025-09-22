import urllib.request
from bs4 import BeautifulSoup
import ssl

# Set up SSL context to bypass certificate verification
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get the starting URL, count, and position from the user
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Repeat the process 'count' times
for i in range(count):
    # Fetch the HTML content of the URL
    html = urllib.request.urlopen(url, context=ctx).read()
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all anchor tags (<a>) on the page
    tags = soup.find_all('a')
    
    # Get the URL at the specified position (position starts at 1, but list indexing starts at 0)
    link = tags[position - 1].get('href', None)
    
    # Print the URL being retrieved
    print(f'Retrieving: {link}')
    
    # Update the URL for the next iteration
    url = link

# After following the links the specified number of times, print the last name
# Extract the last name from the URL by splitting at '/' and removing '.html'
last_name = url.split('/')[-1].replace('known_by_', '').replace('.html', '')
print(f'The answer to the assignment for this execution is "{last_name}".')
