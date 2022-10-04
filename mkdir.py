import os


dirr = input ("what dir: ")
file = input ("what file: ")

os.system ("mkdir "+dirr+" ; cd "+dirr+" ; "+"touch "+file)
print ("okay")
input ("> ")
