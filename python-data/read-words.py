counts = dict()
fhand = input('Which file?: ')
try :
    fname = open(fhand)
except :
    print("that doesn't work!")
for line in fname : 
    line = line.rstrip()
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1

for aaa,bbb in counts.items() :
    print(aaa, bbb)