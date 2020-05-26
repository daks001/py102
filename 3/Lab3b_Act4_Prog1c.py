# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB3B_ACTIVITY4_PROGRAM1c
# Date:		    12 SEPTEMBER 2019

from math import*
#part (c) using Mohr-Coulomb Failure Criterion
print("This program calculates the shear stress given normal stress, cohesion and internal friction")
nstress = float(input("Enter the normal stress in lbf/in^2:")) #normal stress in lbf/in^2
coh = float(input("Enter the cohesion in lbf/in^2:")) #cohesion in lbf/in^2
int_fric = float(input("Enter the internal friction in degrees:")) #angle of internal friction in degrees
sstress = nstress * tan(int_fric) + coh #shear stress in bf/in^2
print("Shear stress: %.4f" %sstress, "lbf/in^2")

