# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB3B_ACTIVITY4_PROGRAM1d
# Date:		    12 SEPTEMBER 2019

#part (d) using Arps Equation
print("This program calculates the production of a well given the initial production and decline rates, and the hyperbolic constant")
time = int(input("Enter the time in days:")) #time in days
ip_rate = float(input("Enter the initial production rate in barrels/day:")) #initial production rate in barrels/day
id_rate = float(input("Enter the initial decline rate in barrels/day:")) #initial decline rate in barrels/day
hyp_const = float(input("Enter the hyperbolic constant:")) #hyperbolic constant: no unit
pro_rate = ip_rate / ((1+ hyp_const * id_rate * time)**(1 / hyp_const)) #production in barrels/day
print("Production of the well after", time, "days is: %.4f" %pro_rate, "barrels/day")


