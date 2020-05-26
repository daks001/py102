# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    MAHIRAH SAMAH
#               MICHAEL MARTIN
# Section:		532
# Assignment:	Lab4b_Program2
# Date:		    19 SEPTEMBER 19

print("This program calculates the Reynold number when the user enters the characteristic velocity of the flow, diameter of the pipe and the fluid kinematic viscosity")
#taking user input
V = float(input("Enter the characteristic velocity of the flow in m/s: "))
d = float(input("Enter the diameter of the pipe in m: "))
v = float(input("Enter the fluid kinematic viscosity in m^2/s: "))
#calculating Reynold number
Re = V*d/v
#using relational operators for finding the type of flow
if Re<2300:
    print(Re, "is the Reynold number for the entered data and the flow is laminar.")
elif Re>=2300 and Re<=2900:
    print(Re, "is the Reynold number for the entered data and the flow is in transition.")
elif Re>2900:
    print(Re, "is the Reynold number for the entered data and the flow is turbulent.")

#end of program