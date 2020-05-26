# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    MAHIRAH SAMAH
#               MICHAEL MARTIN
# Section:		532
# Assignment:	Lab4b_Program4
# Date:		    19 SEPTEMBER 19

from math import*
print("This program finds the roots of a user-entered quadratic equation.")
print("A quadratic equation is of the form Ax^2+Bx+C=0.")
#taking user inputs for the coefficients A,B and C of the quadratic equation
A = float(input("Enter the coefficient A of the equation: "))
B = float(input("Enter the coefficient B of the equation: "))
C = float(input("Enter the coefficient C of the equation: "))

#calculating discriminant to find out if roots will be imaginary
d = (B**2)-(4*A*C)

if A!=0: #2 distinct roots
    if d<0: #imaginary roots
        d = abs(d)
        d = sqrt(d)
        root = -B/(2*A)
        root1 = str(root) + "+" + str(d/(2*A)) +"i"
        root2 = str(root) + "-" + str(d/(2*A)) +"i"
        print("The roots are:",root1,"and",root2)
    else: #no imaginary roots
        root1 = ((-B) + sqrt(d))/(2*A)
        root2 = ((-B) - sqrt(d))/(2*A)
        print("The roots are:", str(root1), "and", str(root2))
elif A==0 and B!=0: #linear equation
    root = (-C)/B
    print("The root is:", str(root))
elif A==0 and B==0:
    if C==0:
        print("All coefficients equal to 0")
    else:
        print("Error: Invalid input for the coefficient C.")

#end of program