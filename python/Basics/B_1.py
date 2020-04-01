'''
Given 2 numbers N and M add both the numbers and check whether the sum is odd or even.
Sample Testcase :
INPUT
9 2
OUTPUT
odd

'''

x=input()
a=x.split()
A,B=int(a[0]),int(a[1])
sum=A+B
if sum%2==0:
	print("even")
else:
	print("odd")