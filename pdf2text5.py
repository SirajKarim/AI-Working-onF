import subprocess

out = subprocess.Popen(['C:/Users/DELL/Desktop/mupdf-1.14.0-windows/mutool.exe', 'show', r"E:\KIET\DS\Book\Introduction to Algorithms 3rd Edition.pdf", 'outline'],
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT)

stdout, stderr = out.communicate()

stdout = str(stdout)

mystr = stdout
mystr = mystr.split(sep=r'\r\n')

i = 0
len_mystr = len(mystr[0])

new_list = []
for s in mystr:
    s = s.replace(r'\t', '  ')
    if i == 0:
        s = s[2:len_mystr]
    new_list.append(s)
    i = i + 1

new_list.pop()

for s in new_list:
    print(s)

import json

# define list with values
basicList = [1, "Cape Town", 4.6]

# open output file for writing
with open('chap1.txt', 'w') as filehandle:
    json.dump(new_list, filehandle)