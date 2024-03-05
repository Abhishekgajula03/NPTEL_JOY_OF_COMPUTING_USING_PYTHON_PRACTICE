"""
* first import string
then  empty dict and data 
then open a file with name file so that you can write ur output
for loop with string.ascii_letters length
dict of 1 st term will be replace with 2 nd char
then open text file which has char which should be convert 
while true read a file  f.read(1)
if no tc  error  if c in dict then dict[c]=data
if example like number cannot be subsitute
then write this contain of data in the file 
print(data)
close file

"""

import string
data=""
dict={}
file=open("open_file.txt","w")
for i in range(len(string.ascii_letters)):
        dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
with open("opentext.txt") as f:
        while True:
            c=f.read(1)
            if not c:
              print("error")
            if c in dict:
              data=dict[c]
            else:
              c=data
            file.write(data)
            print(data)
file.close()
