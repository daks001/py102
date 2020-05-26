# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB 7b PROGRAM 2
# Date:		10 OCTOBER 2019

from math import *

print('This program performs computations on vectors.')
d1 = int(input("Enter the dimension of vector A as an integer: "))
a = []
#taking input foe vector A
for i in range(d1):
    print("You will have to enter coordinate number",str(i+1),"for the vector A.")
    a.append(int(input('Enter here: ')))
d2 = int(input("Enter the dimension of vector B as an integer: "))
b = []
#taking input for vector B
for i in range(d2):
    print("You will have to enter coordinate number", str(i+1), "for the vector B.")
    b.append(int(input('Enter here: ')))
#printing out vectors A and B
print('Vector A is:', a)
print('Vector B is:', b)
sum_a = 0
#calculating the magnitude of vector A
for i in range(d1):
    sum_a += a[i]**2
mag_a = sum_a**0.5
print("The magnitude of vector A is:",mag_a)
sum_b = 0
#calculating the magnitude of vector B
for i in range(d2):
    sum_b += b[i]**2
mag_b = sum_b**0.5
print("The magnitude of vector B is:",mag_b)
apb = []
#calculating the value of A+B, keeping in mind that vectors can be of different dimensions
for i in range(max(d1,d2)):
    if i < len(a) and i < len(b):
        apb.append(a[i] + b[i])
    elif i >= len(a):
        apb.append(b[i])
    elif i>= len(b):
        apb.append(a[i])
print('A+B is: ', apb) #printing A+B
amb = []
#calculating the value of A-B, keeping in mind that vectors can be of different dimensions
for i in range(max(d1,d2)):
    if i < len(a) and i < len(b):
        amb.append(a[i] - b[i])
    elif i >= len(a):
        amb.append(-b[i])
    elif i>= len(b):
        amb.append(a[i])
print('A-B is: ', amb) #printing A-B
