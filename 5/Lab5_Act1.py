# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    MAHIRAH SAMAH
#               MICHAEL MARTIN
# Section:		532
# Assignment:	Lab5_Activity1
# Date:		    24 SEPTEMBER 19

print("This program finds the roots of a cubic polynomial")
#taking inputs for the coefficients of x^3 and x^2
A = float(input("Enter the coefficient of x^3: "))
B = float(input("Enter the coefficient of x^2: "))
C = float(input("Enter the coefficient of x: "))
D = float(input("Enter the constant: "))
#taking inputs for the interval's lower and upper bounds
a = float(input("Enter the lower bound of the interval on x that includes a signle root of the cubic polynomial: "))
b = float(input("Enter the upper bound of the interval on x that includes a signle root of the cubic polynomial: "))
#calculating f of a and f of b
f_a = (A*(a**3))+(B*(a**2))+(C*a)+D
f_b = (A*(b**3))+(b*(a**2))+(C*b)+D
#tol is tolerance
tol = 10e-6
count = 0
p=0
#finding the root of the function using a while loop
while abs(b-a)>tol:
    count += 1
    if f_a<0 and f_b>0 and f_a != 0 and f_b != 0:
        p = (a+b)/2
        f_p = (A*(p**3))+(B*(p**2))+(C*p)+D
        if f_p<0:
            a=p
        elif f_p>0:
            b=p
        else:
            break
    elif f_a>0 and f_b<0 and f_a!=0 and f_b!=0:
        p = (a+b)/2
        f_p = (A*(p**3))+(B*(p**2))+(C*p)+D
        if f_p>0:
            a=p
        elif f_p<0:
            b=p
        else:
            break
    else:
        print("Error")
    #count+=1
#displaying result
print("The root of the function is:",p)
print(count,"is the number of iterations taken")
