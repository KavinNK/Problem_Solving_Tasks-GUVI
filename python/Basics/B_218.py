'''
Given base(B) and height(H) of a triangle find its area.
Input Size : N <= 1000000
Sample Testcase :
INPUT
2 4
OUTPUT
4

'''

A=input()
a=A.split()
B,H = int(a[0]),int(a[1])
area = 0.5*B*H
print(area)