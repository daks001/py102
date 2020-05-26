# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    MAHIRAH SAMAH
#               MICHAEL MARTIN
# Section:		532
# Assignment:	Lab5_Activity2_c
# Date:		    24 SEPTEMBER 19

from math import*
#f1a
tol = 10e-6
x = float(input("Enter the value of x at which the derivative should be evaluated. Enter the angle's value in degrees: "))
x = x * (pi/180)
a = 0.1*(pi/180)
fxa = sin((x+a))
fx = sin(x)
f = (fxa - fx) / a
diff = 1
prev = f
count = 1 #because 1 evaluation has already been done at x = 0.1
while diff>tol:
    count += 1
    prev = f
    a /= 2
    fxa = sin((x + a))
    fx = sin(x)
    f = (fxa - fx) / a
    diff = prev - f

print("sin", x, "is:", f)
print("The calculation takes", count, "iterations")
#f1b
fxa = sin ((x-a))
fx = sin(x)
f = (fx - fxa) / a
diff = 1
prev = f
count = 1 #because 1 evaluation has already been done at x = 0.1
while diff>tol:
    count += 1
    prev = f
    a /= 2
    fxa = sin((x - a))
    fx = sin(x)
    f = (fx - fxa) / a
    diff = prev - f

print("sin", x, "is:", f)
print("The calculation takes", count, "iterations")
#f1c
fxa = sin ((x+a))
fx = sin((x-a))
f = (fxa - fx) / (2*a)
diff = 1
prev = f
count = 1 #because 1 evaluation has already been done at x = 0.1
while diff>tol:
    count += 1
    prev = f
    a /= 2
    fxa = sin((x + a))
    fx = sin((x-a))
    f = (fxa - fx) / (a*2)
    diff = prev - f

print("sin", x, "is:", f)
print("The calculation takes", count, "iterations")

#
#

#f2a
tol = 10e-6
x = float(input("Enter the value of x at which the derivative should be evaluated. Enter the angle's value in degrees: "))
a = 0.1
x = x * (pi/180)
fxa = cos ((x+a))
fx = cos(x)
f = (fxa - fx) / a
diff = 1
prev = f
count = 1 #because 1 evaluation has already been done at x = 0.1
while diff>tol:
    count += 1
    prev = f
    a /= 2
    fxa = cos((x + a))
    fx = cos(x)
    f = (fxa - fx) / a
    diff = prev - f

print("cos", x, "is:", f)
print("The calculation takes", count, "iterations")
#f2b
fxa = cos ((x-a))
fx = cos(x)
f = (fx - fxa) / a
diff = 1
prev = f
count = 1 #because 1 evaluation has already been done at x = 0.1
while diff>tol:
    count += 1
    prev = f
    a /= 2
    fxa = cos((x - a))
    fx = cos(x)
    f = (fx - fxa) / a
    diff = prev - f

print("cos", x, "is:", f)
print("The calculation takes", count, "iterations")
#f2c
fxa = cos ((x+a))
fx = cos((x-a))
f = (fxa - fx) / (2*a)
diff = 1
prev = f
count = 1 #because 1 evaluation has already been done at x = 0.1
while diff>tol:
    count += 1
    prev = f
    a /= 2
    fxa = cos((x + a))
    fx = cos((x-a))
    f = (fxa - fx) / (a*2)
    diff = prev - f

print("cos", x, "is:", f)
print("The calculation takes", count, "iterations")

#
#

#f3a
tol = 10e-6
x = float(input("Enter the value of x at which the derivative should be evaluated. Enter the angle's value in degrees: "))
a = 0.1
x = x * (pi/180)
fxa = tan ((x+a))
fx = tan(x)
f = (fxa - fx) / a
diff = 1
prev = f
count = 1 #because 1 evaluation has already been done at x = 0.1
while diff>tol:
    count += 1
    prev = f
    a /= 2
    fxa = tan((x + a))
    fx = tan(x)
    f = (fxa - fx) / a
    diff = prev - f

print("tan", x, "is:", f)
print("The calculation takes", count, "iterations")
#f3b
fxa = tan ((x-a))
fx = tan(x)
f = (fx - fxa) / a
diff = 1
prev = f
count = 1 #because 1 evaluation has already been done at x = 0.1
while diff>tol:
    count += 1
    prev = f
    a /= 2
    fxa = tan((x - a))
    fx = tan(x)
    f = (fx - fxa) / a
    diff = prev - f

print("tan", x, "is:", f)
print("The calculation takes", count, "iterations")
#f3c
fxa = tan ((x+a))
fx = tan((x-a))
f = (fxa - fx) / (2*a)
diff = 1
prev = f
count = 1 #because 1 evaluation has already been done at x = 0.1
while diff>tol:
    count += 1
    prev = f
    a /= 2
    fxa = tan((x + a))
    fx = tan((x-a))
    f = (fxa - fx) / (a*2)
    diff = prev - f

print("tan", x, "is:", f)
print("The calculation takes", count, "iterations")

#
#

#f4a
tol = 10e-6
x = float(input("Enter the value of x at which the derivative should be evaluated: "))
a = 0.1
fxa = log((x+a),e)
fx = log(x,e)
f = (fxa - fx) / a
diff = 1
prev = f
count = 1 #because 1 evaluation has already been done at x = 0.1
while diff>tol:
    count += 1
    prev = f
    a /= 2
    fxa = log((x+a),e)
    fx = log(x,e)
    f = (fxa - fx) / a
    diff = prev - f

print("log", x, "is:", f)
print("The calculation takes", count, "iterations")
#f4b
fxa = log((x+a),e)
fx = log(x,e)
f = (fx - fxa) / a
diff = 1
prev = f
count = 1 #because 1 evaluation has already been done at x = 0.1
while diff>tol:
    count += 1
    prev = f
    a /= 2
    fxa = log((x+a),e)
    fx = log(x,e)
    f = (fx - fxa) / a
    diff = prev - f

print("log", x, "is:", f)
print("The calculation takes", count, "iterations")
#f4c
fxa = log((x+a),e)
fx = log((x-a),e)
f = (fxa - fx) / (2*a)
diff = 1
prev = f
count = 1 #because 1 evaluation has already been done at x = 0.1
while diff>tol:
    count += 1
    prev = f
    a /= 2
    fxa = log((x+a),e)
    fx = log((x-a),e)
    f = (fxa - fx) / (a*2)
    diff = prev - f

print("log", x, "is:", f)
print("The calculation takes", count, "iterations")