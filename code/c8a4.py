
# Use the file name mbox-short.txt as the file name - romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    for i in line: # observe indentation here
        if i not in lst:
            lst.append(i)
            
lst.sort() # observe indentation here.  this is where i made mistakes..
print(lst)
