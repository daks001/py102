# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    MAHIRAH SAMAH
#               MICHAEL MARTIN
# Section:		532
# Assignment:	Lab5_Activity2_b
# Date:		    24 SEPTEMBER 19

print("This program calculates the derivative of a polynomial numerically")
#taking inputs for the coefficients of x^3 and x^2 and x and the constant
print("A polynomial is of the type Ax^3 + Bx^2 + Cx + D.")
A = float(input("Enter A, the coefficient of x^3: "))
B = float(input("Enter B, the coefficient of x^2: "))
C = float(input("Enter C, the coefficient of x: "))
D = float(input("Enter D, the constant: "))
#inputting the value of x at which the derivative's value is required
x = float(input("Enter the value of x: "))
tol = 10e-6
#f1
a = 0.1
diff = 1
#calculating f(x-a) and f(x) and the limit f
fxa = ((A * ((x + a) ** 3)) + (B * ((x + a) ** 2)) + (C * (x + a)) + D)
fx = ((A * (x ** 3)) + (B * (x ** 2)) + (C * x) + D)
f = (fxa - fx) / a
ori_f = f

prev = 0
count = 1 #because 1 evaluation has already been done for a = 0.1

while diff>(tol):
    count += 1 #incrementing number of iterations
    prev = f
    a /= 2 #splitting a in half
    # calculating f(x-a) and f(x) and the limit f
    fxa = ((A * ((x + a) ** 3)) + (B * ((x + a) ** 2)) + (C * (x + a)) + D)
    fx = ((A * (x ** 3)) + (B * (x ** 2)) + (C * x) + D)
    f = (fxa - fx) / a
    diff = prev - f #diff is the difference between successive evaluations

print("By the first method,")
print("The value of the derivative at", x, "is:", f)
print("This calculation took", count, "iterations")

#f2
a = 0.1
diff = 1
#calculating f(x-a) and f(x) and the limit f
fxa = ((A * ((x - a) ** 3)) + (B * ((x - a) ** 2)) + (C * (x - a)) + D)
fx = ((A * (x ** 3)) + (B * (x ** 2)) + (C * x) + D)
f = (fx - fxa) / a
ori_f = f

prev = 0
count = 1 #because 1 evaluation has already been done for a = 0.1

while diff>(tol):
    count += 1 #incrementing number of iterations
    prev = f
    a /= 2 #splitting a in half
    # calculating f(x-a) and f(x) and the limit f
    fxa = ((A * ((x - a) ** 3)) + (B * ((x - a) ** 2)) + (C * (x - a)) + D)
    fx = ((A * (x ** 3)) + (B * (x ** 2)) + (C * x) + D)
    f = (fx - fxa) / a
    diff = prev - f #diff is the difference between successive evaluations

print("By the second method,")
print("The value of the derivative at", x, "is:", f)
print("This calculation took", count, "iterations")

#f3
a = 0.1
diff = 1
#calculating f(x+a) and f(x-a) and the limit f
fxa = ((A * ((x + a) ** 3)) + (B * ((x + a) ** 2)) + (C * (x + a)) + D)
fx = ((A * ((x - a) ** 3)) + (B * ((x - a) ** 2)) + (C * (x - a)) + D)
f = (fxa - fx) / (2 * a)
ori_f = f

prev = 0
count = 1 #because 1 evaluation has already been done for a = 0.1

while diff>(tol):
    count += 1 #incrementing number of iterations
    prev = f
    a /= 2 #splitting a in half
    # calculating f(x+a) and f(x-a) and the limit f
    fxa = ((A * ((x + a) ** 3)) + (B * ((x + a) ** 2)) + (C * (x + a)) + D)
    fx = ((A * ((x - a) ** 3)) + (B * ((x - a) ** 2)) + (C * (x - a)) + D)
    f = (fxa - fx) / (2 * a)
    diff = prev - f #diff is the difference between successive evaluations

print("By the third method,")
print("The value of the derivative at", x, "is:", f)
print("This calculation took", count, "iterations")

#the values are different for the different expressions




