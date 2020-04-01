'''
Given numbers A,B find A^B.
Input Size : 1 <= A <= 5 <= B <= 50
Sample Testcase :
INPUT
3 4
OUTPUT
81

'''

x=input()
a=x.split()
A,B=int(a[0]),int(a[1])
print(A**B)