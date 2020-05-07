
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
lst = list()
di = dict()

 
for line in fh :
	if line.startswith('From '):
		line = line.rstrip()
		line = line.split()
		#print (line)
		str = line[5]
		#print (str)
		hour = str[0:2]
		#print (str.find(":"))
		#print (hour)
		di[hour] = di.get(hour,0) + 1

#print (di)
		
for key, val in di.items():
	lst.append((key,val))
lst.sort()
for val,key in lst:
	print (val,key)