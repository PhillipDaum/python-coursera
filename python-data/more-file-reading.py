astr = "X-DSPAM-Confidence:"
astr_len = len(astr)
count = 0
amount = 0


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
for line in fhand:
    line = line.rstrip()
    if not line.startswith(astr):
        continue
    count = count + 1
    num = float(line[astr_len: ])
    amount = amount + num
    average = amount/count
print("Average spam confidence:", average)