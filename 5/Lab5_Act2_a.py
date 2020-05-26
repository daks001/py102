# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    MAHIRAH SAMAH
#               MICHAEL MARTIN
# Section:		532
# Assignment:	Lab5_Activity2_a
# Date:		    24 SEPTEMBER 19

print("This program calculates the derivative of a polynomial analytically")
#taking inputs for the coefficients of x^3 and x^2 and x and the constant
print("A polynomial is of the type Ax^3 + Bx^2 + Cx + D.")
A = float(input("Enter A, the coefficient of x^3: "))
B = float(input("Enter B, the coefficient of x^2: "))
C = float(input("Enter C, the coefficient of x: "))
D = float(input("Enter D, the constant: "))

a = A * 3
b = B * 2
#inputting the value of x at which the derivative's value is required
x = float(input("Enter the value of x: "))

ax = a * (x**2)
bx = b * x
cx = C
#computing the value of the derivative at given x
val = ax + bx + cx

print("The value of the derivative", x, "is:", val)