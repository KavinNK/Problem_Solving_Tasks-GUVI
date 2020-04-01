'''
Given a number N, print 'yes' if it is composite else print 'no'.
Sample Testcase :
INPUT
123
OUTPUT
yes

'''


import math

n = int(input())

if n < 2:
    print("no")
    quit()
elif n == 2:
    print("no")
    quit()

i = 2
limit = int(math.sqrt(n))

while i <= limit:
    if n % i == 0:
        print("yes")
        quit()
    i += 1

print("no")