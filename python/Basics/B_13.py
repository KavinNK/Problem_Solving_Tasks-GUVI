'''
Given 2 numbers N,M. Print 'yes' if their product is a perfect square else print 'no'.
Sample Testcase :
INPUT
5 5
OUTPUT
yes
'''


import math
L = input()
a=L.split()
I,J=int(a[0]),int(a[1])
product=I*J
root = math.sqrt(product)
if int(root + 0.5) ** 2 == product:
    print("yes")
else:
    print("no")