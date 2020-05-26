# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB2B_PROGRAM1
# Date:		    05 SEPTEMBER 2019

from math import *
#program 1
#part (a)
name = str("Dakshika Srivastava")
uin = 228009279
engr_sec = 532
print("My name is:", name)
print("My UIN is:", uin)
print("The section of ENGR 102 that I'm in is:", engr_sec)

#part (b)
fact = str("I've been involved in robotics and that got me interested in coding")
print("An interesting fact about me is:", fact)

#part(c) using Ohm's Law
res = 20 #resistance in ohm
cur = 5 #current in A, that is, ampere
vol = res * cur #voltage in V, that is, volt
print("Voltage across the conductor is:", vol, "volt")

#part (d) using Kinetic Energy
mass = 100 #mass of object in kg
vel = 21 #velocity of object in m/s
kine = 0.5 * mass * (vel**2) #kinetic energy of object in J, that is, joule
print("Kinetic energy of the object is:", kine, "joule")

#part (e) using Reynolds Number
vel = 100 #velocity in m/s
kvis = 1.2 #kinematic viscosity in (m^2)/s
lin_dim = 2.5 #linear dimension in m
re_num = vel * lin_dim / kvis #reynolds Number: dimensionless
print("Reynolds number for the fluid is:", re_num)

#part (f) using Arps Equation
time = 20 #time in days
ip_rate = 100 #initial production rate in barrels/day
id_rate = 2 #initial decline rate in barrels/day
hyp_const = 0.8 #hyperbolic constant: no unit
pro_rate = ip_rate / ((1+ hyp_const * id_rate * time)**(1 / hyp_const)) #production in barrels/day
print("Production of the well after", time, "days is:", pro_rate, "barrels/day")

#part (g) using Mohr-Coulomb Failure Criterion
nstress = 20 #normal stress in lbf/in^2
coh = 2 #cohesion in lbf/in^2
int_fric = 35 #angle of internal friction in degrees
sstress = nstress * tan(int_fric) + coh #shear stress in bf/in^2
print("The shear stress is:", sstress, "lbf/in^2")
