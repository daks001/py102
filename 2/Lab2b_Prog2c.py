# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB2B_PROGRAM2c
# Date:		    06 SEPTEMBER 2019

#time=13 for (1,3,7)
t1 = 13
x1 = 1
y1 = 3
z1 = 7
#time=84 for (23,-5,10)
t2 = 84
x2 = 23
y2 = -5
z2 = 10
#setting initial, in-between and ending time of interpolation
ta = 20
tb = 27.5
tc = 35
td = 42.5
te = 50
#estimating (x0,y0,z0) at time=ta
x0 = (x2 - x1) * (ta - t1) / (t2 - t1) + x1
y0 = (y2 - y1) * (ta - t1) / (t2 - t1) + y1
z0 = (z2 - z1) * (ta - t1) / (t2 - t1) + z1
print("x coordinate is:", x0)
print("y coordinate is:", y0)
print("z coordinate is:", z0)
print("--------------------------------------")
#estimating (x0,y0,z0) at time=tb
x0 = (x2 - x1) * (tb - t1) / (t2 - t1) + x1
y0 = (y2 - y1) * (tb - t1) / (t2 - t1) + y1
z0 = (z2 - z1) * (tb - t1) / (t2 - t1) + z1
print("x coordinate is:", x0)
print("y coordinate is:", y0)
print("z coordinate is:", z0)
print("--------------------------------------")
#estimating (x0,y0,z0) at time=tc
x0 = (x2 - x1) * (tc - t1) / (t2 - t1) + x1
y0 = (y2 - y1) * (tc - t1) / (t2 - t1) + y1
z0 = (z2 - z1) * (tc - t1) / (t2 - t1) + z1
print("x coordinate is:", x0)
print("y coordinate is:", y0)
print("z coordinate is:", z0)
print("--------------------------------------")
#estimating (x0,y0,z0) at time=td
x0 = (x2 - x1) * (td - t1) / (t2 - t1) + x1
y0 = (y2 - y1) * (td - t1) / (t2 - t1) + y1
z0 = (z2 - z1) * (td - t1) / (t2 - t1) + z1
print("x coordinate is:", x0)
print("y coordinate is:", y0)
print("z coordinate is:", z0)
print("--------------------------------------")
#estimating (x0,y0,z0) at time=te
t0 = 54
x0 = (x2 - x1) * (te - t1) / (t2 - t1) + x1
y0 = (y2 - y1) * (te - t1) / (t2 - t1) + y1
z0 = (z2 - z1) * (te - t1) / (t2 - t1) + z1
print("x coordinate is:", x0)
print("y coordinate is:", y0)
print("z coordinate is:", z0)
print("--------------------------------------")