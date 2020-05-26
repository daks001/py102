# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:      	DAKSHIKA SRIVASTAVA
# 	        	MAHIRAH SAMAH
# 	        	MIKE MARTIN
# Section:    	532
# Assignment: 	Lab10_Act2
# Date:       	29 OCTOBER 2019

#importing libraries
import math
import matplotlib.pyplot as plt
import numpy as np

#part 1
x=np.arange(-2,2,0.01) #list of x values
y2 = [] #to store y values for f=2
y6 = [] #to store y values for f=6
#appending the y values for each x to y2 and y6
for i in x:
    y2.append((i**2)/(4*2))
    y6.append((i**2)/(4*6))
plt.plot(x, y2, linewidth=2) #plot for f=2
plt.plot(x, y6, color='purple', linewidth=4) #plot for f=6
#specifying the plot title and x and y axis labels
plt.suptitle('Parabola plots for varying Focal Lengths. Blue is for f=2 and purple is for f=6')
plt.ylabel('y values')
plt.xlabel('x values')
plt.show()

#part 2
#initialising the a,b,c,d variables
a = 2
b = 3
c = -11
d = -6
x = np.linspace(-4,4,num=25) #list of x values
y=[] #to store the y values
for i in x:
    y.append((a*(i**3))+(b*(i**2))+(c*i)+d) #appending the y values for each x
plt.plot(x, y, 'o') #plot
#specifying the plot title and x and y axis labels
plt.suptitle('Plot of Cubic Polynomial')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()

#part 3
x = np.arange(-2*math.pi, 2*math.pi, 0.001) #list of x values
ys = [] #to store sin(x)
yc = [] #to store cos(x)
for i in x:
    ys.append(math.sin(i)) #appending y values of sin(x) for each x
    yc.append(math.cos(i)) #appending y values of cos(x) for each x
plt.plot(x, ys, linewidth=2) #plot of sin(x)
plt.plot(x, yc, color='red', linewidth=2) #plot of cos(x)
#specifying the plot title and x and y axis labels
plt.suptitle('Plot of sin(x) and cos(x). Blue is for sine and red is for cosine.')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()

#end of program