# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    MAHIRAH SAMAH
#               MICHAEL MARTIN
#               JAMES GONZALEZ
# Section:		532
# Assignment:	Lab4_Activity2
# Date:		    17 SEPTEMBER 19

from math import*
print("This program calculates the total fee given the number of hours the car was parked")
#inputting the number of hours
hours = float(input("Enter the "
                    " the car is parked in the garage. \nEnter as negative if the ticket is lost. \nEnter here: "))
#accounting for lost tickets, hence negative input
neg=0
if hours<0:
    neg=1
else:
    neg=0
#rounding up the number of hours (positive)
hours = abs(hours)
hours = ceil(hours)
hours = int(hours)
charge=0
days=hours/24
days=int(days)
rem_hours = hours%24
print(rem_hours)
#calculating the total charge based on the number of hours the car was parked
if rem_hours>=0 and rem_hours<=2:
    charge=4
elif rem_hours>2 and rem_hours<=4:
    charge=4+3
elif rem_hours>4:
    charge= 4+3+(rem_hours-4)

if neg==1:
    charge=36+charge

if days!=0:
    charge=charge+(24*days)
    if neg==1:
        print("Parked for", days, "days and", str(rem_hours), "hours but lost ticket; pay: $"+ str(charge))
    if neg == 0:
        print("Parked for", days, "days and", str(rem_hours), "hours; pay: $"+ str(charge))
else:
    if neg==1:
        print("Parked for", rem_hours, ("hours but lost ticket; pay: $"+str(charge)))
    if neg==0:
        print("Parked for", rem_hours, ("hours; pay: $" + str(charge)))