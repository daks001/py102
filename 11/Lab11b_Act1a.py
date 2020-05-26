# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	Lab 11b Activity 1(a)
# Date:		    8 NOVEMBER 2019

import math #to use pi
#creatign a function to calculate the volume of the material remianing
def volume(l,b,h,r):
    vol = None
    if r < min(l/2, b/2): #for radius within range
        vol = (l*b*h) - (math.pi*r*r*h)
    else: #for greater radius
        vol = - (l*b*h) + (math.pi*r*r*h)
    return vol

#taking input
l = float(input('Enter the length of the box: '))
b = float(input('Enter the breadth of the box: '))
h = float(input('Enter the height of the box: '))
r = float(input('Enter the radius of the hole: '))
#calling the function
vol = volume(l,b,h,r)
print('The volume of the material remaining is:',vol)