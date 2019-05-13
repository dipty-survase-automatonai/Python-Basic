#!/usr/bin/python
def add(a,b,c=0,d=0):
	return a+b+c+d
if __name__=='__main__':
	a=eval(input("enter a:"))
	b=eval(input("enter b:"))
	c=eval(input("enter c:"))
	d=eval(input("enter d:"))
	print("add",add(a,b,c))
