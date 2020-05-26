# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:      	DAKSHIKA SRIVASTAVA
# 	        	MAHIRAH SAMAH
# 	        	MIKE MARTIN
# Section:    	532
# Assignment: 	Lab8_Activity2
# Date:       	15 OCTOBER 2019

#finding the coordinates: p and q of the 2 nearest x values
min1 = min(tol) #the 1st nearest x value
min_i = tol.index(min1) #index of min in tol to be able to find in xl and yl
tol.pop(min_i) #removing 1st minimum difference to find second
min2 = min(tol) #2nd nearest x value
min2_i = tol.index(min2) #indec of min2 in tol to be able to find in xl and yl
p = [xl[min_i], yl[min_i]] #the first point for interpolation
xl.pop(min_i) #removing first x of min(tol)
yl.pop(min_i) #removing first y of min(tol)
q = [xl[min2_i], yl[min2_i]] #the second point for interpolation