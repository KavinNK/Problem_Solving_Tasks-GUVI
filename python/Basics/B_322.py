'''
Given a string S consisting of 2 words reverse the order of two words .
Input Size : |S| <= 10000000
Sample Testcase :
INPUT
hello world
OUTPUT
world hello

'''

x=input()
z=x.split()
A,B=z[0],z[1]
print("{} {}".format(B,A))
