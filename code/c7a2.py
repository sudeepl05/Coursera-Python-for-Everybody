
# Use the file name mbox-short.txt as the file name - mbox-short.txt

fname = input("Enter file name: ")
fh = open(fname)
tot = 0
cnt = 0 
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
	txt_l = len("X-DSPAM-Confidence:") 
    num = float(line[txt_l:])
    tot = tot + num
    cnt = cnt + 1

avg = tot/cnt
print("Average spam confidence:", avg)
