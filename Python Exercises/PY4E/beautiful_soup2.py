import urllib.request
from bs4 import BeautifulSoup
import ssl

# Set up SSL context to bypass SSL verification
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt the user for the URL
# http://py4e-data.dr-chuck.net/comments_2059913.html
url = input('Enter - ')

# Retrieve HTML from the URL
html = urllib.request.urlopen(url, context=ctx).read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all <span> tags with class 'comments'
tags = soup.find_all('span', class_='comments')

# Initialize variables to store the sum and count
total_sum = 0
count = 0

# Loop through each <span> tag, extract the number, and add to the sum
for tag in tags:
    number = int(tag.text)  # Convert the text to an integer
    total_sum += number
    count += 1

# Output the count of numbers and the total sum
print(f'Count {count}')
print(f'Sum {total_sum}')
