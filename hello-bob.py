astr = input('Enter a number:')
# if the line below gets a traceback, it does the other thing
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('second', istr)