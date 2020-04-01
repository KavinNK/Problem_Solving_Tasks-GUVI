'''
Given 3 numbers A,B,C print 'yes' if they can form the sides of a right angled triangle,otherwise 'no'.
Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes

'''

X=input()
a=X.split()
x,y,z = int(a[0]),int(a[1]),int(a[2])
if x**2+y**2==z**2:
    print('yes')
else:
    print('no')