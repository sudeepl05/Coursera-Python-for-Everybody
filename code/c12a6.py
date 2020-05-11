#http://py4e-data.dr-chuck.net/comments_42.html
#http://py4e-data.dr-chuck.net/comments_498475.html

import urllib.request, urllib.parse, urllib.error

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Initialising the count and total
count = 0
total = 0

# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter link: ")
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/comments_498475.html"

html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    # Trying to convert the tag's content into integer
    try:
        total = total + int(tag.contents[0])
        count = count + 1
    except:
        continue

# Printing the results
print('Count',count)
print('Sum',total)