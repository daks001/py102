# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:      	DAKSHIKA SRIVASTAVA
# 	        	MAHIRAH SAMAH
# 	        	MIKE MARTIN
# Section:    	532
# Assignment: 	Lab12_Act2
# Date:       	12 NOVEMBER 2019

import numpy as np
def enter():
    a = float(input('Enter the starting limit of the interval: '))
    b = float(input('Enter the ending limit of the interval: '))
    return [a, b]

#f = x^6 + 7x^5 - 23x^3 + 47x -11
coeff = [1, 7, 0, -23, 0, 47, -11]
limits = enter()
# x = np.linspace(limits[0], limits[1], num=10) #initial x values

def mid_interval():
    count = 1 #not 0 bc 1 iteration is being done outside the while loop where count increments
    #limit is a list
    inter = 10*2 #num interval
    x = np.linspace(limits[0], limits[1], num=10)
    j = 0
    summ = 0
    a = len(coeff) - 1
    y = []
    for i in range(len(x)):
        # area =
        summ = 0
        j = 0
        a = len(coeff) - 1
        for k in range(len(coeff)):
            if a != 0:
                summ += coeff[j] * x[i] ** a
            else:
                summ += coeff[j]
            a -= 1
            j += 1
        y.append(summ)  # appending x value for each x
        summ = 0
    #calculating area
    area = []
    for i in range(len(x)-1):
        area.append(y[i]*((x[i+1]-x[i])/2))
    difference = []
    for i in range(len(area)-1):
        difference.append(area[i+1]-area[i])
    minimum = min(difference)
    tol = 10e-6
    if minimum < tol:
        return (x,area,count)
    else:
        while minimum >= tol:
            x = np.linspace(limits[0], limits[1], num=inter)
            inter *= 2
            area = []
            j = 0
            summ = 0
            a = len(coeff) - 1
            y = []
            for i in range(len(x)):
                # area =
                summ = 0
                j = 0
                a = len(coeff) - 1
                for k in range(len(coeff)):
                    if a != 0:
                        summ += coeff[j] * x[i] ** a
                    else:
                        summ += coeff[j]
                    a -= 1
                    j += 1
                y.append(summ)  # appending x value for each x
                summ = 0
            for i in range(len(x) - 1):
                area.append(y[i] * ((x[i + 1] - x[i])/2))
            difference = []
            for i in range(len(area) - 1):
                difference.append(area[i + 1] - area[i])
            minimum = min(difference)
            count += 1
        return (area, x, count)
    # return (x,y,area)

######################################################################

def beg_interval():
    count = 1
    #limit is a list
    inter = 10*2 #num interval
    x = np.linspace(limits[0], limits[1], num=10)
    j = 0
    summ = 0
    a = len(coeff) - 1
    y = []
    for i in range(len(x)):
        # area =
        summ = 0
        j = 0
        a = len(coeff) - 1
        for k in range(len(coeff)):
            if a != 0:
                summ += coeff[j] * x[i] ** a
            else:
                summ += coeff[j]
            a -= 1
            j += 1
        # print(summ)
        y.append(summ)  # appending x value for each x
        summ = 0
    #calculating area
    area = []
    for i in range(len(x)-1):
        area.append(y[i]*x[i])
    difference = []
    for i in range(len(area)-1):
        difference.append(area[i+1]-area[i])
    minimum = min(difference)
    tol = 10e-6
    if minimum < tol:
        return (x,area,count)
    else:
        while minimum >= tol:
            x = np.linspace(limits[0], limits[1], num=inter)
            inter *= 2
            area = []
            j = 0
            summ = 0
            a = len(coeff) - 1
            y = []
            for i in range(len(x)):
                # area =
                summ = 0
                j = 0
                a = len(coeff) - 1
                for k in range(len(coeff)):
                    if a != 0:
                        summ += coeff[j] * x[i] ** a
                    else:
                        summ += coeff[j]
                    a -= 1
                    j += 1
                # print(summ)
                y.append(summ)  # appending x value for each x
                summ = 0
            for i in range(len(x) - 1):
                area.append(y[i] *  x[i])
            difference = []
            for i in range(len(area) - 1):
                difference.append(area[i + 1] - area[i])
            minimum = min(difference)
            count += 1
        return (area,x,count)
    # return (x,y,area)


########################################################################

def end_interval():
    count = 1
    #limit is a list
    inter = 10*2 #num interval
    x = np.linspace(limits[0], limits[1], num=10)
    j = 0
    summ = 0
    a = len(coeff) - 1
    y = []
    for i in range(len(x)):
        # area =
        summ = 0
        j = 0
        a = len(coeff) - 1
        for k in range(len(coeff)):
            if a != 0:
                summ += coeff[j] * x[i] ** a
            else:
                summ += coeff[j]
            a -= 1
            j += 1
        y.append(summ)  # appending x value for each x
        summ = 0
    #calculating area
    area = []
    for i in range(1,len(x)):
        area.append(y[i]* x[i])
    difference = []
    for i in range(len(area)-1):
        difference.append(area[i+1]-area[i])
    minimum = min(difference)
    tol = 10e-6
    if minimum < tol:
        return (x,area,count)
    else:
        while minimum >= tol:
            x = np.linspace(limits[0], limits[1], num=inter)
            inter *= 2
            area = []
            j = 0
            summ = 0
            a = len(coeff) - 1
            y = []
            for i in range(len(x)):
                # area =
                summ = 0
                j = 0
                a = len(coeff) - 1
                for k in range(len(coeff)):
                    if a != 0:
                        summ += coeff[j] * x[i] ** a
                    else:
                        summ += coeff[j]
                    a -= 1
                    j += 1
                # print(summ)
                y.append(summ)  # appending x value for each x
                summ = 0
            for i in range(1, len(x) ):
                area.append(y[i] * x[i])
            difference = []
            for i in range(len(area) - 1):
                difference.append(area[i + 1] - area[i])
            minimum = min(difference)
            count += 1
        return (area,x,count)
    # return (x,y,area)

########################################################################

def trap_interval():
    count = 1
    #limit is a list
    inter = 10*2 #num interval
    x = np.linspace(limits[0], limits[1], num=10)
    j = 0
    summ = 0
    a = len(coeff) - 1
    y = []
    for i in range(len(x)):
        # area =
        summ = 0
        j = 0
        a = len(coeff) - 1
        for k in range(len(coeff)):
            if a != 0:
                summ += coeff[j] * x[i] ** a
            else:
                summ += coeff[j]
            a -= 1
            j += 1
        y.append(summ)  # appending x value for each x
        summ = 0
    #calculating area
    area = []
    for i in range(len(x)-1):
        area.append(0.5 * (y[i] + y[i+1]) * (x[i+1] - x[i]))
    difference = []
    for i in range(len(area)-1):
        difference.append(area[i+1]-area[i])
    minimum = min(difference)
    tol = 10e-6
    if minimum < tol:
        return (x,area,count)
    else:
        while minimum >= tol:
            x = np.linspace(limits[0], limits[1], num=inter)
            inter *= 2
            area = []
            j = 0
            summ = 0
            a = len(coeff) - 1
            y = []
            for i in range(len(x)):
                # area =
                summ = 0
                j = 0
                a = len(coeff) - 1
                for k in range(len(coeff)):
                    if a != 0:
                        summ += coeff[j] * x[i] ** a
                    else:
                        summ += coeff[j]
                    a -= 1
                    j += 1
                y.append(summ)  # appending x value for each x
                summ = 0
            for i in range(len(x) - 1):
                area.append(0.5 * (y[i] + y[i+1]) * (x[i+1] - x[i]))
            difference = []
            for i in range(len(area) - 1):
                difference.append(area[i + 1] - area[i])
            minimum = min(difference)
            count += 1
        return (area,x,count)
    # return (x,y,area)

def integrate(area_list):
    return sum(area_list)

#calling the functions
result = mid_interval()
print(integrate(result[0]))
print('Number of iterations was',result[2])
result = beg_interval()
print(integrate(result[0]))
print('Number of iterations was',result[2])
result = end_interval()
print(integrate(result[0]))
print('Number of iterations was',result[2])
result = trap_interval()
print(integrate(result[0]))
print('Number of iterations was',result[2])