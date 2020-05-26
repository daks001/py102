# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB 10b ACTIVITY 1
# Date:		    31 OCTOBER 2019

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
#creating the vector list and the matrix
v = np.array([[1],[0]])
vn = v
x = []
y = []
m = np.array([[1.00583, -0.087156], [0.087156, 1.00583]])
plt.plot(vn[0], vn[1])
#fiinding the different points
for i in range(250):
    vn = np.dot(m,v)
    v = vn
    print(vn)
    x.append(vn[0])
    y.append(vn[1])
#plotting the points
plt.plot(x,y)
#formatting the plot title and axes labels
plt.suptitle('A spiral curve')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()
