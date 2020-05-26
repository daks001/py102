# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB3B_ACTIVITY4_PROGRAM1a
# Date:		    12 SEPTEMBER 2019

#part(a) using Ohm's Law
print("This program calculates voltage given current and resistance")
res = float(input("Enter the resistance across the circuit in ohm:")) #resistance in ohm
cur = float(input("Enter the current in the conductor in ampere:")) #current in A, that is, ampere
vol = res * cur #voltage in V, that is, volt
print("Voltage: %.4f" %vol, "volt")

