'''
Given an array of N elements switch(swap) the element with the adjacent element and print the output.
Sample Testcase :
INPUT
5
3 2 1 2 3
OUTPUT
2 3 2 1 3

'''

A=int(input())
B=input()
b=B.split()
for i in range(0,A-1,2):
	temp = b[i]
	b[i] = b[i+1]
	b[i+1] = temp
for i in range(0,A):
	if(i == A-1):
		print(b[i])
	else:
		print(b[i],end=" ")
		
	