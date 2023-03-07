import re

f = open('preproinsulin-seq.txt','r')
content = f.read()
#print(content)
f.close()
newcontent = re.sub(r'\/\/|\s|\r|\n|\d+|ORIGIN', '', content)
    
print(len(newcontent))

f = open('preproinsulin-seq-clean.txt','w')
f.write(newcontent)

f = open("lsinsulin-seq-clean.txt", "x")
isinsulin = newcontent[0:24]
f.write(isinsulin)
print(len(isinsulin))

f = open("binsulin-seq-clean.txt", "x")
binsulin = newcontent[24:54]
f.write(binsulin)
print(len(binsulin))

f = open("cinsulin-seq-clean.txt", "x")
cinsulin = newcontent[54:89]
f.write(cinsulin)
print(len(cinsulin))

f = open("ainsulin-seq-clean.txt", "x")
ainsulin = newcontent[89:110]
f.write(ainsulin)
print(len(ainsulin))