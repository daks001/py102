# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:      	DAKSHIKA SRIVASTAVA
# 	        	MAHIRAH SAMAH
# 	        	MIKE MARTIN
# Section:    	532
# Assignment: 	Lab8_Activity2
# Date:       	15 OCTOBER 2019

#using interpolation to find the y coordinate
#the x coordinate is given and is stored in x
#calculating the slope of the equation
#slope = (y2-y1)/(x2-x1)
m = (q[1]-p[1]) / (q[0]-p[0])
#estimating the y coordinate
#using the point slope form of equation of line
#y = mx + c
y = m * (x-p[0]) + p[1]