''' You will be provided with a number. Print the number of days in the month corresponding to that number.

Note: In case the input is February, print 28 days. If the Input is not in valid range print "Error".

Input Description:
The input is in the form of a number.

Output Description:
Find the days in the month corresponding to the input number. Print Error if the input is not in a valid range.

Sample Input :
8
Sample Output :
31 '''

Num = int(input())
if Num ==0 or Num>12:
	print("Error")
elif (Num == 2):
	print("28")
elif Num ==4 or Num==6 or Num == 9 or Num<11:
	print("30")
else:
	print("31")