'''
Given a number N and an array of N elements, find the Bitwise OR of the array elements.
Input Size : N <= 100000
Sample Testcase :
INPUT
2
2 4
OUTPUT
6
'''

n=int(input())
A=input()
a=list(map(int, A.strip().split()))
def AND(a, n) :  
    ans = a[0] 
    for i in range(n) : 
        ans |= a[i] 
          
    return ans 
print(AND(a, n)) 