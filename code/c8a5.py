
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
lst = list()
count=0
 
for line in fh :
    line = line.rstrip()
    if not line.startswith('From '): continue        
    words = line.split()
    print(words[1])
    count +=1

print("There were", count, "lines in the file with From as the first word")
