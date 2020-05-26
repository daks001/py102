# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:      	DAKSHIKA SRIVASTAVA
# 	        	MAHIRAH SAMAH
# 	        	MIKE MARTIN
# Section:    	532
# Assignment: 	Lab10_Act1
# Date:       	29 OCTOBER 2019

#As a team, we have gone through all required sections of the tutorial, and each team member understands the material.

#importing library
import numpy as np
#initialising matrices
A=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
B=np.array([[1,2],[3,4],[5,6],[7,8]])
C=np.array([[1,2,3],[4,5,6]])
D=np.array([[1],[2],[3]])
#printing the matrices
print(A)
print(B)
print(C)
print(D)
#finding E=ABC
E = A.dot(B.dot(C))
print(E)
#print transpose of E
print(E.transpose())
#finding inverse of E to find x
F=np.linalg.inv(E)
x=F.dot(D)
print(x)
#end of program