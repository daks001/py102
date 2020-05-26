# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB2B_PROGRAM3
# Date:		    05 SEPTEMBER 2019

#printing z as 1
x = 1
y = 10
z = 0
z += x #x1 y10 z1
print(z) #as 1

#printing z as 3
x += 1 #x2 y10 z1
z += x #x2 y10 z3
print(z) #as 3

#printing z as 11
x = 1 #x1 y10 z3
z = 0 #x1 y10 z3
z += x #x1 y10 z1
z += y #x1 y10 z11
print(z) #as 11

#printing z as 28
x += 1 #x2 y10 z11
y += x #x2 y12 z11
y *= x #x2 y24 z11
x = y #x24 y24 z11
z = 0 #x24 y24 z0
x += 1 #x25 y24 z0
x += 1 #x26 y24 z0
x += 1 #x27 y24 z0
x += 1 #x28 y24 z0
z += x #x28 y24 z28
print(z) #as 28

#printing z as 123
x = 1 #x1 y24 z28
y = 10 #x1 y0 z28
z = 0 #x1 y10 z0
x = y #x10 y10 z0
x += 1 #x11 y10 z0
x += 1 #x12 y10 z0
y *= x #x12 y120 z0
x = 1 #x1 y120 z0
x += 1 #x2 y120 z0
x += 1 #x3 y120 z0
y += x #x3 y123 z0
z += y #x3 y123 z123
print(z) #as 123

#printing z as 10^32
y = 10 #x3 y10 z123
x = y #x10 y10 z123
i = 1
while i<=31:
    y *= x
    i += 1
#x10 y10e32 z123
z = 0 #x10 y10e32 z123
z += y #x10 y10e32 z10e32
print(z) #as 10e32

#printing z as 4321
x = 1 #x1 y10e32 z10e32
y = 10 #x1 y10 z10e32
z = 0 #x1 y10 z0
x += 1 #x2 y10 z0
x += 1 #x3 y10 z0
x += 1 #x4 y10 z0
y *= x #x4 y40 z0
x = y #x40 y40 z0
y = 10 #x40 y10 z0
y *= x #x40 y400 z0
x = y #x400 y400 z0
y = 10 #x400 y10 z0
y *= x #x40 y4000 z0
z += y #x40 y4000 z4000
y = 10 #x40 y10 z4000
x = 1 #x1 y10 z4000
x += 1 #x2 y10 z4000
x += 1 #x3 y10 z4000
y *= x #x3 y30 z4000
x = y #x30 y30 z4000
y = 10 #x30 y10 z4000
y *= x #x30 y300 z4000
z += y #x30 y300 z4300
x = 1 #x1 y300 z4300
x += 1 #x2 y300 z4300
y = 10 #x2 y10 z4300
y *= x #x2 y20 z4300
z += y #x2 y20 z4320
x = 1 #x1 y20 z4320
z += x #x1 y20 z4321
print(z) #as 4321
