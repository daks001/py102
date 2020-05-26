# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB 10b ACTIVITY 2
# Date:		    31 OCTOBER 2019

#importing libraries
import matplotlib.pyplot as plt
data = open('WeatherDataMac.csv', 'r') #opening the weather data file
l = []
for i in data:
    l.append(i.split(','))
# print(l)
for i in range(1,len(l)):
    for j in range(1,14):
        l[i][j]=float(l[i][j]) #converting all weather statistics from string to float
#to store the respective weather values
avg_temp = []
avg_press = []
avg_dew = []
prec = []
date = []
temp_high = []
temp_low = []
#appending data to the previously created empty lists
for i in range(1, len(l)):
    temp_high.append(l[i][1])
    temp_low.append(l[i][3])
    avg_temp.append(l[i][2])
    avg_press.append(l[i][-3])
    prec.append(l[i][-1])
    avg_dew.append(l[i][5])
    date.append(l[i][0])
#plotting  the line graoh
fig, ax1 = plt.subplots()
ax2 = ax1.twinx() #to have 2 different y axes for the same x axis
p1 = ax1.plot(date, avg_temp)
p2 = ax2.plot(date, avg_press)
ax1.set_ylabel('Average temperature')
ax2.set_ylabel("Average pressure")
plt.title('Average pressure and temperature vs time period')
plt.xlabel('Date')
plt.show()

#plotting the histogram
plt.hist(prec, range=(0,9))
plt.title('Average precipitation amounts')
plt.xlabel('Precipitation level')
plt.ylabel('Number of days with that precipitation value')
plt.show()

#plotting the scatter plot
plt.scatter(avg_temp, avg_dew)
plt.title('Relationship between average temperature and average dew point')
plt.xlabel('Average temperature')
plt.ylabel("Average dew point")
plt.show()

#plotting the bar graph with the error bars
d = 1
sum_temp = 0
high = []
low = []
avg_temp = []
temp_high = []
temp_low = []
for i in range(36):
    for j in range(1, len(l)):
        if int(l[j][0][0]) == d or (l[j][0][1]!='/' and int(l[j][0][0]+l[j][0][1]) == d):
            sum_temp += l[j][2]
            high.append(l[j][1])
            low.append(l[j][3])
    temp_high.append(max(high))
    temp_low.append(min(low))
    avg_temp.append(sum_temp/len(high))
    high = []
    low = []
    sum_temp = 0
    if d==12:
        d = 1
    elif d<12:
        d += 1
ta = []
th = []
tl = []
for i in range(0, 12):
    th.append((float(temp_high[i])+float(temp_high[i+12])+float(temp_high[i+24]))/3)
    tl.append(float(temp_low[i])+float(temp_low[i+12])+float(temp_low[i+24])/3)
    ta.append(float(avg_temp[i]) + float(avg_temp[i + 12]) + float(avg_temp[i + 24]) / 3)
x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.bar(x, ta, yerr=[th, tl], capsize=5)
plt.title('Average temperature and error plot')
plt.xlabel('Months')
plt.ylabel('Average temperature and low and high temperature error bars')
plt.show()