import mmap

f = open('barra.txt')
s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
if s.find('ireland') != -1:
    print('true')
raw_input ()
