'''
Let P represent Paper, R represent Rock and S represent Scissors. Given 2 out of the 3 determine which one wins. If its a draw print 'D'.
Sample Testcase :
INPUT
R P
OUTPUT
P

'''

x=input()
c=x.split()
A,B = c[0],c[1]
def RPS(a,b):
	if A==B:
		return("D")
	elif A=="P" and B== "R" or A=="R" and B== "P":
		return("P")
	elif A=="S" and B== "P" or A=="P" and B== "S":
		return("S")
	elif A=="R" and B== "S" or A=="S" and B== "R":
		return("R")
print(RPS(A,B))