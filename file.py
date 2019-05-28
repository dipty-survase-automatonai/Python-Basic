#!/usr/bin/python
import io
x=input("enter file name:")
#fd=io.FileIO(x)
fd=open(x)
line=fd.readline()
while line!=b'':
	print(line)
	line=fd.readline()







