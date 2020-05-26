# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB 5b ACTIVITY b
# Date:		26 SEPTEMBER 2019

print("This program calculates the sum of al numbers from 0 upto the number eneterd and product of those from 1 to that entered, using both for and while loops.")
#taking input for the number
n = int(input("Enter a number: "))
#initiating sum to 0 and product to 1
sum = 0
pro = 1
for i in range(0,n+1):
    sum += i
    if (i!=0):
        pro *= i

print("Using a for loop, sum is", sum, "and product is", pro)
#initializing i for while loop
i = 0
#reinitializing sum and pro
sum = 0
pro = 1
while i<=n:
    sum += i
    if (i!=0):
        pro *= i
    i += 1
print("Using a while loop, sum is", sum, "and product is", pro)