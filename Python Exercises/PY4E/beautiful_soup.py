import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Create an SSL context to ignore certificate verification
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt user for a URL
url = input('Enter - ')

# Fetch the HTML content of the URL
html = urllib.request.urlopen(url, context=ctx).read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all anchor tags (<a>)
tags = soup('a')

# Print the 'href' attribute of each anchor tag
for tag in tags:
    print(tag.get('href', None))
