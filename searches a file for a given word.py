import os
import os.path

x = raw_input ('Search for what: ')
for fname in os.listdir('.'):
    if os.path.isfile(fname):
        f = open(fname)
        if x in f.read():
            print fname
        f.close()
kw = raw_input ('Which file would you like to read: ')
with open(kw, 'r') as f:
    content = f.read()
    print content.index(x)
raw_input ()
