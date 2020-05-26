#importing numpy
import numpy as np
import matplotlib.pyplot as plt

#initializing variables
coeff = [1, -3, -5.5, 25]
x = np.arange(-3, 5, 0.0001)
minima = []
maxima = []
yval = []

#creating a function to find the derivative of a polynomial
def diff(c):
    nc = []
    back = len(c)-1
    for i in range(len(c)):
        nc.append(c[i]*back)
        back -= 1
    del nc[-1]
    return nc

#to store the information of the differentiated function
dcoeff = diff(coeff)
dback = len(dcoeff) - 1
y = 0
#finding yvalues for derivative
for i in range(len(x)):
    dback = len(dcoeff) - 1
    for j in range(len(dcoeff)):
        if dback == 0:
            y += dcoeff[j]
        else:
            y += dcoeff[j] * x[i] ** dback
        dback -= 1
    yval.append(y)
    y = 0

mback = len(coeff)-1
yvalues = []
y = 0
#finding yvalues for original function
for i in range(len(x)):
    mback = len(coeff) - 1
    for j in range(len(coeff)):
        if mback == 0:
            y += coeff[j]
        else:
            y += coeff[j] * (x[i] ** mback)
        mback -= 1
    yvalues.append(y)
    y = 0
#finding maxima and minima
for i in range(1, len(yvalues)-1):
    if yvalues[i]>yvalues[i-1] and yvalues[i]>yvalues[i+1]:
        maxima.append([x[i], yvalues[i]])
    if yvalues[i]<yvalues[i-1] and yvalues[i]<yvalues[i+1]:
        minima.append([x[i], yvalues[i]])
#printing results
print('The maxima are:',maxima)
print('The minima are:',minima)

plt.plot(x,yvalues, label='graph')
for i in range(len(maxima)):
    plt.plot(maxima[i][0], maxima[i][1], 'ro')
for i in range(len(minima)):
    plt.plot(minima[i][0], minima[i][1], 'bo')
plt.title('y vs x, Red is maxima and blue is minima')
plt.ylabel('y values')
plt.xlabel('x values')
plt.legend()
plt.show()