# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:      	DAKSHIKA SRIVASTAVA
# 	        	MAHIRAH SAMAH
# 	        	MIKE MARTIN
# Section:    	532
# Assignment: 	Lab8_Activity2
# Date:       	15 OCTOBER 2019
if dx != 0:  # checking for error caused because of division by zero
    dy = y2 - y1
    slope = dy / dx
    x = float(input("Enter the x-coordinate: "))
    y = slope * (x - x1) + y1  # calculating the y-value given the x-value
    print('The y-coordinate is:', y)
else:
    print("Division by zero error.") 