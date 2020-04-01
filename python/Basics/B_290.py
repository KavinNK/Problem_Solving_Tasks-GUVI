'''
Given a number N followed by N numbers.Find the smallest number and largest number and print both the indices(1 based indexing).
Input Size : N <= 100000
Sample Testcase :
INPUT
5
1 2 3 4 5
OUTPUT
1 5

'''

N=int(input())
M=input()
a=M.split()
A=min(a)
B=max(a)
print(a.index(A)+1,end=" ")
print(a.index(B)+1)