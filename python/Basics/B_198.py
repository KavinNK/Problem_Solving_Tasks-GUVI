'''
Given 3 numbers A,B,C print 'yes' if they can form the sides of a scalene triangle else print 'no'.
Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes

'''

A=input()
a=A.split()
x,y,z=int (a[0]),int (a[1]),int (a[2])
if x == y == z:
	print("no")
elif x==y or y==z or z==x:
	print("no")
else:
	print("yes")
