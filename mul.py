#!/usr/bin/python
def multiplication(a,b,c=1,d=1):
	return a*b*c*d
if __name__=='__main__':
	a=eval(input("enter a:"))
	b=eval(input("enter b:"))
	c=eval(input("enter c:"))
	d=eval(input("enter d:"))
	print("multiplication",multiplication(a,b,c,d))
