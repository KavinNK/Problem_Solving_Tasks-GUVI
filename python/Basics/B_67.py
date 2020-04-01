'''
Given a string 'S' swap the even and odd characters starting from index 1(Assume the index starts from 0).
Input Size : |s| <= 10000000(complexity O(n))
Sample Testcase :
INPUT
codekata
OUTPUT
ocedakat


'''

B=input()
def split(B): 
    return [char for char in B] 
b=split(B)
A=len(b)
for i in range(0,A,2):
	temp = b[i]
	b[i] = b[i+1]
	b[i+1] = temp
for i in range (0,A):
	print(b[i],end="")
	