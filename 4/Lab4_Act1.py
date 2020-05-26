# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    MAHIRAH SAMAH
#               MICHAEL MARTIN
#               JAMES GONZALEZ
# Section:		532
# Assignment:	Lab4_Activity1
# Date:		    17 SEPTEMBER 19

#part 1
from math import*
print("This program introduces 'tolerances")
TOL=1e-10 #part 2 using tolerance
a=1/7
print("a is:",a)
b=a*7
print("b is:",b)

a=1/7
print("a is:",a)
b=7*a
print("b is:",b)
c=2*a
d=5*a
e=c+d
print("e is:",e)
if abs(b-e)<TOL:
    print("b and e are equal within tolerance of", TOL)
else:
    print("b and e are NOT equal within tolerance of", TOL)

x=sqrt(1/3)
print("x is:",x)
y=x*x*3
print("y is:",y)
z=x*3*x
print("z is:",z)
if abs(y-z)<TOL:
    print("y and z are equal within tolerance of", TOL)
else:
    print("y and z are NOT equal within tolerance of", TOL)

print("The results were surprising, YES!!!")
