# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    TREVOR YOUNG
# 	 		    JOEY QUISMORIO
#			    AUSTIN GURGOS
# Section:		532
# Assignment:	Lab2_Activity3
# Date:		    05 09 19


from math import *
time1 = 30
time2 = 45
dist1 = 50
dist2 = 615
time = 37
#calculating position of car at any time instant
dist = ((time2 - time)/(time2 - time1)*dist1 + (time1 -  time)/(time1 - time2)*dist2)
print("The car would be",dist,'meters past the starting line of the track after',time,'seconds')
#optional challenge
peri = 2*pi*500
while dist>peri:
    dist = dist - peri
print("The car would be",dist,'meters past the starting line of the track after',time,'seconds')
