import re
file=input("enter file name here: ")
a=list()
counter=0
open_file=open(file,'r')
for line in open_file:
    line = line.rstrip()
    counts=re.findall('[0-9]+',line)
    if len(counts) == 0: continue
    a+= counts
print(a)
for count in a:
    counter=counter+int(count)
print(counter)