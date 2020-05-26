# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	Lab 11b Activity 1(e)
# Date:		    8 NOVEMBER 2019

#creating a function to return the min, max and mean of a list
def calc(a):
    return 'The minimum value is '+str(min(a))+' and the maximum value is '+str(max(a))+' and the mean is '+str((sum(a)/len(a)))
#taking input
l = (input('Enter a list of numbers: ')).split()
for i in range(len(l)):
    l[i] = float(l[i])
#calling the function
print(calc(l))