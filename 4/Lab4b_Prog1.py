# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    MAHIRAH SAMAH
#               MICHAEL MARTIN
# Section:		532
# Assignment:	Lab4b_Program1
# Date:		    19 SEPTEMBER 19

print("This program calculates the largest of 3 entered numbers.")
#taking input for the 3 numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
#using relational operators to find the largest number
if a>b and a>c:
    print(a,"is the largest number")
elif b>c and b>a:
    print(b,"is the largest number")
elif c>b and c>a:
    print(c,"is the largest number")
else:
    print("All numbers are same")

#end of program