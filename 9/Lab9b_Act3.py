# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB 9b ACTIVITY 3
# Date:		    26 OCTOBER 2019

data = open('WeatherDataMac.csv', 'r') #opening the weather data file
l = []
for i in data:
    l.append(i.split(','))
for i in range(1,len(l)):
    for j in range(1,14):
        l[i][j]=float(l[i][j]) #converting all weather statistics from string to float
temp_high = [] #to store all temp_high values
temp_low = [] #to store all temp_low values
prec = [] #to store all precipitation values
for i in range(1,len(l)):
    temp_high.append(l[i][1])
    temp_low.append(l[i][3])
    prec.append(l[i][-1])
max_t = max(temp_high) #finding max temp high
min_t = min(temp_low) #finding min temp low
print("The minimum temp is:",min_t)
print("The maximum temp is:",max_t)
print("The average daily precipitaion is:", (sum(prec)/len(prec))) #calculating average daily precipitation
start = 0
end = 0
#finding starting and ending indices for the month of july 2015
for i in range(1,len(l)):
    if '7/1/2015' in l[i][0]:
        start = i
    if '7/31/2015' in l[i][0]:
        end = i
t = [] #to store daily temp high for july 2015
h = [] #to store daily avg humidity for july 2015
prec=[] #to store daily precipitation for july 2015
for i in range(start,end+1):
    t.append(l[i][1])
    h.append(l[i][8])
    prec.append(l[i][-1])
print("For July 2015, the average high temperature is:", (sum(t)/len(t)))
count = 0 #to store number of days with humidity abouve 80%
for i in h:
    if i>=80:
        count+=1 #incrementing count
print("For July 2015, percentage of days when humidity was above 80% is", (count*100/len(h)))
mean = sum(prec)/len(prec)
add = 0
for i in prec:
    add+= (mean-i)**2
sd = ((add)/(len(prec)-1))**0.5 #standard deviation for precipitation values
print("For July 2015, the mean of precipitation levels is",mean,'in. and the standard deviation is',sd,'in')