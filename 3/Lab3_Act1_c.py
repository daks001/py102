# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    MAHIRAH SAMAH
#               MICHAEL MARTIN
# Section:		532
# Assignment:	Lab3_Activity1_c
# Date:		    10 SEPTEMBER 19
print("This program converts pascals to millimeters of mercury")
pascals = float(input("Enter the number of pascals:"))
mmhg = pascals * 0.00750062 #converting mm of hg to pascal
print(pascals,"pascal is equivalent to: %.4f" %mmhg , "millimeters of hg")