# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:      	DAKSHIKA SRIVASTAVA
# 	        	MAHIRAH SAMAH
# 	        	MIKE MARTIN
# Section:    	532
# Assignment: 	Lab12_Act1
# Date:       	12 NOVEMBER 2019

#imorting packages
import matplotlib.pyplot as plt
import numpy as np
#to return to coefficients of the polynomial equation
def coeff():
    '''To return the coefficients of the polynomial equation'''
    print('Enter the coefficients of the polynomial in descending order.')
    print('Enter 0 when a certain degree does not exist')
    print('For example, for x^3 + x -7, you would enter, 1,0,1,-7 just separtaed with a space instead of the comma.')
    c = (input('Enter list here: ')).split()
    for i in range(len(c)):
        c[i]=int(c[i])
    return c

def der(c):
    '''To find the first order derivative'''
    #derivative 1 is df and 2 is ddf
    # c = coeff()
    df = []
    j = len(c)-1
    for i in range(len(c)):
        df1 = c[i]*j
        df.append(df1)
        j -= 1
    del df[-1]
    return df

def der2(l):
    '''To find the double order derivative'''
    ddf = []
    length = len(ddf)
    j = len(l) - 1
    for i in range(len(l)):
        if l[i]!=0:
            df2 = l[i] * j
            ddf.append(df2)
        j -= 1
    del ddf[-1]
    return ddf

def p():
    '''To plot the function, its derivative, second order derivative and the maxima and minima'''
    x = np.arange(-5,5,0.01)
    l1 = coeff()
    l2 = der(l1)
    l3 = der2(l2)
    y1 = []
    y2 = []
    y3 = []
    a = len(l1)-1 #power
    j = 0 #index
    b = len(l2)-1
    c = len(l3)-1
    summ = 0
    for i in range(len(x)): #x values
        j = 0
        a = len(l1)-1
        for k in range(len(l1)):
            if a!=0:
                summ += l1[j]*x[i]**a
            else:
                summ += l1[j]
            a -= 1
            j += 1
        y1.append(summ) #appending x value for each x
        summ = 0
    j = 0
    summ = 0
    for i in range(len(x)):  # x values
        j = 0
        b = len(l2) - 1
        for k in range(len(l2)):
            # print('i',i,'k',k,'j',j,'b',b)
            # if l2[j] != 0:
            if b!=0:
                summ += l2[j] * x[i] ** b
            else:
                summ += l2[j]
            # else:
            #     summ += l2[-1]
            b -= 1
            j += 1
        y2.append(summ)  # appending x value for each x
        summ = 0
    j = 0
    summ = 0
    for i in range(len(x)):  # x values
        j = 0
        c = len(l3) - 1
        for k in range(len(l3)):
            if c != 0:
                summ += l3[j] * x[i] ** c
            else:
                summ += l3[j]
            c -= 1
            j += 1
        y3.append(summ)  # appending x value for each x
        summ = 0
    maxima=[]
    minima=[]
    for i in range(1,len(y1)-1):
        if y1[i]>y1[i-1] and y1[i]>y1[i+1]:
            #this is the maxima
            maxima.append([x[i],y1[i]])
        if y1[i]<y1[i-1] and y1[i]<y1[i+1]:
            minima.append([x[i], y1[i]])
    for i in range(len(maxima)):
        plt.plot(maxima[i][0],maxima[i][1], 'ro')
    for i in range(len(minima)):
        plt.plot(minima[i][0],minima[i][1], 'go')
    plt.plot(x, y1, color='red')
    plt.plot(x, y2, color='yellow')
    plt.plot(x, y3, color='blue')
    plt.ylim(top=15, bottom=-15)
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('y vs x values')
    plt.show()

p() #calling the function