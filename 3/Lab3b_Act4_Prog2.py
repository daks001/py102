# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB3B_ACTIVITY4_PROGRAM1b
# Date:		    12 SEPTEMBER 2019

#program 2
from math import*
print("This program calculates the angle between two 3D vectors")
#inputting observer's coordinates
x0 = float(input("Enter the x coordinate for the position of the observer:"))
y0 = float(input("Enter the y coordinate for the position of the observer:"))
z0 = float(input("Enter the z coordinate for the position of the observer:"))
#inputting coordinates of point 1
x1 = float(input("Enter the x coordinate for the position of point 1:"))
y1 = float(input("Enter the y coordinate for the position of point 1:"))
z1 = float(input("Enter the z coordinate for the position of point 1:"))
#inputting coordinates of point 2
x2 = float(input("Enter the x coordinate for the position of point 2:"))
y2 = float(input("Enter the y coordinate for the position of point 2:"))
z2 = float(input("Enter the z coordinate for the position of point 2:"))
#v1 is point 1 - observer
v1x = x1-x0
v1y = y1-y0
v1z = z1-z0
#v2 is point 2 - observer
v2x = x2-x0
v2y = y2-y0
v2z = z2-z0
#calculating magnitude of v1 and v2
mag_p1 = ((v1x**2)+(v1y**2)+(v1z**2))**0.5
mag_p2 = ((v2x**2)+(v2y**2)+(v2z**2))**0.5
#finding unit vector along v1
x_unit_p1 = v1x / mag_p1
y_unit_p1 = v1y / mag_p1
z_unit_p1 = v1z / mag_p1
#finding unit vector along v2
x_unit_p2 = v2x / mag_p2
y_unit_p2 = v2y / mag_p2
z_unit_p2 = v2z / mag_p2
#calculating dot product of v1 and v2 and then the angle between them in degrees
dot_pro = x_unit_p1 * x_unit_p2 + y_unit_p1 * y_unit_p2 + z_unit_p1 * z_unit_p2
angle = acos(dot_pro)
angle = angle*180/pi
#printing the results
print("Observer location is: x=", x0, "y=", y0, "z=", z0)
print("Point 1 location is: x=", x1, "y=", y1, "z=", z1)
print("Point 2 location is: x=", x2, "y=", y2, "z=", z2)
print("The angle between the points is: %.2f" %angle , "degrees")