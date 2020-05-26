# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:      	DAKSHIKA SRIVASTAVA
# 	        	MAHIRAH SAMAH
# 	        	MIKE MARTIN
# Section:    	532
# Assignment: 	Lab8_Activity2
# Date:       	15 OCTOBER 2019

#using linear interpolation to find y coordinate for any given x coordinate
from math import *
print("This program uses linear interpolation to find the y value for a given x value, given a set of points.")
#taking user input for x coordinates
xl = (input('Enter a list of x-coordinates separated by a space: ')).split()
for i in range(len(xl)):
    xl[i] = float(xl[i]) #converting input from string to float
#taking user input for y coordniates
yl = (input('Enter a list of y-coordinates separated by a space: ')).split()
for i in range(len(yl)):
    yl[i] = float(yl[i]) #converting input from string to float
x = float(input('Enter the x-value whose y-value is required: '))
tol = [] #to store the difference between the enetered x and each previous x coordinate in xl
for i in xl:
    tol.append(abs(x-i)) #taking aboslute of difference to find the nearest x
min1 = min(tol) #the 1st nearest x value
min_i = tol.index(min1) #index of min in tol to be able to find in xl and yl
tol.pop(min_i) #removing 1st minimum difference to find second
min2 = min(tol) #2nd nearest x value
min2_i = tol.index(min2) #indec of min2 in tol to be able to find in xl and yl
p = [xl[min_i], yl[min_i]] #the first point for interpolation
xl.pop(min_i) #removing first x of min(tol)
yl.pop(min_i) #removing first y of min(tol)
q = [xl[min2_i], yl[min2_i]] #the second point for interpolation
if q[0]-p[0]==0:
    print('Error: division by zero')
else:
    m = (q[1]-p[1]) / (q[0]-p[0]) #slope
    y = m * (x-p[0]) + p[1] #estimating the y coordinate
    print("The y coordinate is:",y)
#end of program
