'''
Given 2 numbers N,M find the GCD of N and M.If it cannot be found for given number(s) then print -1
Sample Testcase :
INPUT
10 5
OUTPUT
5

'''
# dosent pass testcases output works fine #

X=input()
A=X.split()
a,b = int(A[0]),int(A[1])
y=min(a,b)
x=max(a,b)
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a,b = int(A[0]),int(A[1])
GCD=gcd(a,b)
if GCD==1:
    print("-1")
else:
    print(GCD)