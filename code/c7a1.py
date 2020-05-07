
fname = input("Enter file name:")
fh = open(fname)

for lx in fh:
	lx = lx.upper()
	lx = lx.rstrip()
	print(lx)