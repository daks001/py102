#importing libraries
import numpy as np
from math import *
import matplotlib.pyplot as plt

#making function gauss
def gauss(x,u,s):
    num = - ((x-u)**2)
    den = 2 * s * s
    ex = np.exp(num/den)
    root = (2 * pi * s * s) ** 0.5
    return root*ex

#initializing the variables
u = 0
s = 1
x = np.arange(-3, 3, 0.0001)
y = []
for i in x:
    y.append(gauss(i,u,s))

#plotting the graph
plt.plot(x, y)
plt.title('The Gaussian Function')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()

###############################################################

from ENGR102 import isprime
#taking user input
n1 = int(input("Enter an integer"))
n2 = int(input("Enter another integer"))
#specifying the starting and ending points for the 'for' loop
start = min(n1, n2)
if start%2 == 0:
    #even number for starting point
    start = start + 1
end = max(n1, n2)
prime = [] #to store prime numbers
for i in range(start, end+1, 2):
    if isprime(i)==True:
        prime.append(i)
#checking if any prime number was found
if len(prime)>0:
    print(y)
else:
    print('No prime numbers found in the specified interval.')

###############################################################

#making a function
def zero(x):
    less = 0 #to store number of numbers which are less than 0
    #checking if input array is empty
    if len(x)==0:
        return [-1, -1]
    else:
        for i in x:
            if i<0:
                less += 1
        frac = less / len(x) #calculating fraction of numbers in the list which are negative
        return [less, frac]

###############################################################

