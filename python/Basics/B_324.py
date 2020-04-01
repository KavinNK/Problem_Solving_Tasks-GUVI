'''
Shapur has to find weaknesses in the roman army to defeat them. So he gives the army a weakness number. In Shapur's opinion the weakness of an army is equal to the number of triplets i, j, k such that i < j < k and ai > aj > ak where ax is the power of man standing at position x. The Roman army has one special trait — powers of all the people in it are distinct. Help Shapur find out how weak the romans are.
Input Size : N<=100000
Example:
INPUT
3
3 2 1
OUTPUT
1

'''

N=int(input())
Y=input()
a=Y.split()
count=0
def isWeakertriplet(a,b,c):
	if A>B and B>C:
		return True
	return False
for i in range (0,N-2):
	A,B,C = int(a[i]),int(a[i+1]),int(a[i+2])
	if(isWeakertriplet(A,B,C)):
		count=count+1
print(count)      
      
      