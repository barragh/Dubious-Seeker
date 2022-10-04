import os
from os.path import join

lookfor = input ("> ")
for root, dirs, files in os.walk('C:\\'):
    print ("searching", root)
    if lookfor in files:
        print ("found: %s" % join(root, lookfor))
        break
