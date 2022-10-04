import os
from os.path import join

lookfor = input ("WHAT DO YOU WANT?> ")
for root, dirs, files in os.walk('C:\\'):
    directory = os.listdir(root)
    print ("searching", root)
    if lookfor in files:
        fil = open("List.txt", "a+")
        fnd = ("found: %s" % join(root, lookfor))
        print (fnd)
        fil.write(fnd+ "\n")
        print (directory)
        fil.write (directory)
        file.close ()
        break
