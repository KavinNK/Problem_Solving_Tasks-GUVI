'''
Given 3 numbers N , L and R. Print 'yes' if N is between L and R else print 'no'.
Sample Testcase :
INPUT
3
2 6
OUTPUT
yes
'''


N = int(input())
L = input()
a=L.split()
I,J=int(a[0]),int(a[1])
X=max(I,J)
Y=min(I,J)
if N<Y or N>X:
	print("no")
elif N>Y and N<X:
	print("yes")
	