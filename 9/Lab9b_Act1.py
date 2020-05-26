# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB 9b ACTIVITY 1
# Date:		    26 OCTOBER 2019

#opening the text file
c = open('Celsius.txt', 'r')
#creating a new text file
f = open('Fahrenheit.txt', 'w')
t = []
#converting string to float for conversion calculation
for i in c:
    t.append(float(i.strip()))
#writing the fahrenheit values to the new text file
for i in t:
    f.write(str(i*1.8+3.2)+'\n')