# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB 6 PROGRAM b
# Date:		    3 OCTOBER 2019

print("This program calculates stress when strain is given.")
strain = float(input("Enter the value of strain: "))

#A=(0,0) B=(0.0125,42.8) C=(0.0575,44) D=(0.18,51) E=(0.2625,60)
#initializing x and y coordinates of points A, B, C, D and E
ax = 0
ay = 0
bx = 0.0125
by = 42.8
cx = 0.0575
cy = 44
dx = 0.18
ey = 51
ex = 0.2625
dy = 60
ymod = 0 #young's modulus
stress = 0 #final stress value
flag = 0 #to track whether the input value for stress is within range

#Formula used: stress - x = slope (strain - y) and slope = ymod

if strain>=ax and strain<=bx:
    ymod = (by-ay)/(bx-ax)
    stress = (ymod * (strain - ax)) + ay
elif strain>bx and strain<=cx:
    ymod = (cy-by)/(cx-bx)
    stress = (ymod * (strain - bx)) + by
elif strain>cx and strain<=dx:
    ymod = (dy-cy)/(dx-cx)
    stress = (ymod * (strain - cx)) + cy
elif strain>dx and strain<=ex:
    ymod = (ey-dy)/(ex-dx)
    stress = (ymod * (strain - dx)) + dy
else:
    print('Out of range.')
    flag = 1

if flag == 0:
    print("The stress for the given strain is:", stress, "Pa")
#else if flag is 1 'Out of range' has already been output to the screen
