# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	Lab 11b Activity 1(f)
# Date:		    8 NOVEMBER 2019

#creating a function to find velocity given time abd distance, for many values
def velocity(time,dist):
    vel = []
    #appending velocities for each time difference
    for i in range(1, len(time)):
        vel.append((dist[i]-dist[i-1])/(time[i]-time[i-1]))
    return vel
#taking input
d = (input('Enter a list of distance values: ')).split()
for i in range(len(d)):
    d[i] = float(d[i])
t = (input('Enter a list of time values: ')).split()
for i in range(len(t)):
    t[i] = float(t[i])
#calling the function
print(velocity(t,d))