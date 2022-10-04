import os
import os.path

x = raw_input ('Search for what: ')
for fname in os.listdir('.'):
    if os.path.isfile(fname):
        f = open(fname)
        if x in f.read():
            print fname
        f.close()
print ''
f = raw_input ('Which file would you like to read: ')
with open(f, "r") as f:
    searchlines = f.readlines()
for i, line in enumerate(searchlines):
    if x in line: 
        for l in searchlines[i:i+3]: print l,
        print
