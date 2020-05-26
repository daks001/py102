# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB3B_ACTIVITY4_PROGRAM1b
# Date:		    12 SEPTEMBER 2019

#part (b) using Kinetic Energy
print("This program calculates the kinetic energy given mass and velocity")
mass = float(input("Enter the mass of the object in kg:")) #mass of object in kg
vel = float(input("Enter the velocity of the object in m/s:")) #velocity of object in m/s
kine = 0.5 * mass * (vel**2) #kinetic energy of object in J, that is, joule
print("Kinetic energy: %.4f" %kine, "joule")



