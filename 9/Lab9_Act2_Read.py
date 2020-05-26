# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:      	DAKSHIKA SRIVASTAVA
# 	        	MAHIRAH SAMAH
# 	        	MIKE MARTIN
# Section:    	532
# Assignment: 	Lab9_Act2
# Date:       	22 OCTOBER 2019

inp = input('Enter the file name: ') #taking file name input
data = open(inp, 'r') #opening that file

for i in data:
    print(i.rjust(10), end='') #printing the data in a table format