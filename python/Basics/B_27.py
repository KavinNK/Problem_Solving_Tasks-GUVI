'''
Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.
Sample Testcase :
INPUT
6 2
1 2 3 5 7 8
OUTPUT
0

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
if count<1:
	print("-1")
else:
	print(count-1)

