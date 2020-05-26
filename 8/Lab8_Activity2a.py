# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:      	DAKSHIKA SRIVASTAVA
# 	        	MAHIRAH SAMAH
# 	        	MIKE MARTIN
# Section:    	532
# Assignment: 	Lab8_Activity2
# Date:       	15 OCTOBER 2019

#taking and formatting user input
#x coordinates
xl = (input('Enter a list of x-coordinates: ')).split()
for i in range(len(xl)):
    xl[i] = float(xl[i]) #converting input type
#y coordinates
yl = (input('Enter a list of y-coordinates: ')).split()
for i in range(len(yl)):
    yl[i] = float(yl[i]) #converting input type
x = float(input('Enter x-value: '))