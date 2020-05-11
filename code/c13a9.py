# http://py4e-data.dr-chuck.net/comments_42.json
# http://py4e-data.dr-chuck.net/comments_498478.json

# Importing libraries
import urllib.request, urllib.parse, urllib.error
import json

# Initialising
total_count = 0

# Asking user to input the source URL of the XML data file
url = input('Enter URL: ')
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/comments_498478.json"
print('Retrieving',url)

uhandle = urllib.request.urlopen(url)
data = uhandle.read()

#Transforming json data
info = json.loads(data)

# Getting data in comments
for comment in info['comments']:
	try:
		total_count = total_count + int(comment['count'])
	except:
		continue

#Generating print
print('Retrieved', len(data),'characters')
print('Count', len(info['comments']))
print('Sum', total_count)
