import os
from os.path import join
file = open("results.txt", "a+")
file.close ()
keyword = input("Search For?: ")  # ask the user for keyword, use raw_input() on Python 2.x

root_dir = 'C:\\'  # path to the root directory to search
for root, dirs, files in os.walk(root_dir, onerror=None):  # walk the root dir
    directory = os.listdir (root)
    for filename in files:  # iterate over the files in the current dir
        file_path = os.path.join(root, filename)  # build the file path
        try:
            with open(file_path, "rb") as f:  # open the file for reading
                # read the file line by line
                for line in f:  # use: for i, line in enumerate(f) if you need line numbers
                    try:
                        line = line.decode("utf-8")  # try to decode the contents to utf-8
                    except ValueError:  # decoding failed, skip the line
                        continue
                    if keyword in line:  # if the keyword exists on the current line...
                        print(" ")
                        print(line)      #print the line.
                        print(" ")
                        print(file_path)  # print the file path
                        print(directory) #print the contents of the direc the file is in.
                        file = open("results.txt", "a+")
                        find = root+" "+filename
                        find2 = line
                        file.write(find+ "\n")
                        file.write(find2+ "\n")
                        file.close ()
                    elif keyword in filename:
                        print(" ")
                        print ("found: %s" % join(root, filename))
                        print (directory)
                        print(" ")
                        file = open("results.txt", "a+")
                        fnd = root+" "+filename
                        fnd2 = directory
                        file.write(fnd+ "\n")
                        file.write(''.join(fnd2)+ "\n")
                        file.close ()
                         # no need to iterate over the rest of the file
        except (IOError, OSError):  # ignore read and permission errors
            pass
