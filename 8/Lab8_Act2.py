# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:      	DAKSHIKA SRIVASTAVA
# 	        	MAHIRAH SAMAH
# 	        	MIKE MARTIN
# Section:    	532
# Assignment: 	Lab8_Activity2
# Date:       	15 OCTOBER 2019

print('This program finds the y value for a given x-value using the equation of a line')
#taking user input
x1 = float(input("Enter the x-coordinate for the first point: "))
y1 = float(input("Enter the y-coordinate for the first point: "))
x2 = float(input("Enter the x-coordinate for the second point: "))
y2 = float(input("Enter the y-coordinate for the second point: "))
#checking for an edge case if the user enters the coordinates in a type other than floating type
if type(x1) is float or type(x2) is float or type(y1) is float or type(y2) is float:
    dx = x2-x1
    if dx!=0: #checking for edge case and error caused because of division by zero
        dy = y2-y1
        m =  dy/dx
        x = float(input("Enter the x-coordinate for which you need the y value: "))
        y = m*(x-x1)+y1 #calculating the y-value given the x-value
        print('The y-coordinate is:',y)
    else:
        print("Division by zero: math error.")
else:
    print("Invalid input")

