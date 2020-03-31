'''
Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.
Sample Testcase :
INPUT
4 2
1 2 3 3
OUTPUT
yes

'''


A=input()
B=input()
count=0
a=A.split()
N,K=int (a[0]),int (a[1])
b=B.split()
for i in range(0,N):
	if K==int(b[i]):
		count = count+1
	else:
		count = count
if count>=1:
	print("yes")
else:
	print("no")
       