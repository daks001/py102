# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:      	DAKSHIKA SRIVASTAVA
# 	        	MAHIRAH SAMAH
# 	        	MIKE MARTIN
# Section:    	532
# Assignment: 	Lab11_Act1
# Date:       	5 NOVEMBER 2019

#creating function F(float)
def F(x):
    f = 6*x**4-8*x**3+2*x**2+11*x-7 # a complex function whose roots are not known
    return f

#creating function deriv(float)
def deriv(x):
    fx = F(x)
    a = 10e-10
    fxa = F(x-a)
    dx = (fx-fxa)/a #finding derivative
    return dx

#creating function newton_step(float)
def newton_step(guess):
    f = F(guess)
    dx = deriv(guess)
    new_guess = guess - (f/dx)
    return new_guess

#creating function newton(float)
def newton(guess):
    x0 = guess
    xi = newton_step(x0)
    val = [xi]
    global counter #declaring counter as global to be able to print it later
    counter = 0
    while (abs(newton_step(xi)-newton_step(x0))>10e-6): #while difference is within tolerance
        counter += 1
        x0 = xi
        xi = newton_step(xi)
        val.append(xi)
    return val
print(newton(5))
print('Newton method takes',counter,'iterations.')


################################################################################################
#the bisection method with the same function:


tol = 10e-6
#f1
a = 0.1
diff = 1
x = 5
#calculating f(x-a) and f(x) and the limit f
fxa = ((6 * ((x + a) ** 4)) - (8 * ((x + a) ** 3)) + (2 * (x + a) ** 3) + (11 * (x + a)) - 7)
fx = 6*x**4-8*x**3+2*x**2+11*x-7
f = (fxa - fx) / a
ori_f = f

prev = 0
count = 1 #because 1 evaluation has already been done for a = 0.1

while diff>(tol):
    count += 1 #incrementing number of iterations
    prev = f
    a /= 2 #splitting a in half
    # calculating f(x-a) and f(x) and the limit f
    fxa = ((6 * ((x + a) ** 4)) - (8 * ((x + a) ** 3)) + (2 * (x + a) ** 3) + (11 * (x + a)) - 7)
    fx = 6*x**4-8*x**3+2*x**2+11*x-7
    f = (fxa - fx) / a
    diff = prev - f #diff is the difference between successive evaluations

print("By the first method,")
print("The value of the derivative at", x, "is:", f)
print("This calculation took", count, "iterations")

