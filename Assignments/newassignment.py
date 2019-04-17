ANO=11

import os

fname="Assignment {}".format(ANO)
fname=os.path.abspath(fname)
if not os.path.exists(fname):
    os.makedirs(fname)
else:
    print("Folder Already Created:Exiting...")
    exit()
filename="Assignment{}_".format(ANO)
fname=os.path.join(fname,filename)
#print(fname)

for i in range(5):
    fd=open("{}{}.py".format(fname,i+1),mode="x")

# Read in the file
with open('newassignment.py', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('ANO=12', 'ANO={}'.format(ANO+1))

# Write the file out again
with open('newassignment.py', 'w') as file:
  file.write(filedata)
