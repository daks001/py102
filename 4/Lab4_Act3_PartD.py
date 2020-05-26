# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB4_ACTIVITY3_PartD
# Date:		    18 SEPTEMBER 2019

print("This is the optional part of Lab 4, activity 3")
#user input for a
aval = input("For a, enter 'True' or 'T' or 't' for true and 'False' or 'F' or 'f' for false: ")
#assigning boolean values to variable a depending on user input
if aval=='True' or aval=='T' or aval=='t':
    a = True
elif aval=='False' or aval=='F' or aval=='f':
    a = False

#user input for b
bval = input("For b, enter 'True' or 'T' or 't' for true and 'False' or 'F' or 'f' for false: ")
#assigning boolean values to variable b depending on user input
if bval=='True' or bval=='T' or bval=='t':
    b = True
elif bval=='False' or bval=='F' or bval=='f':
    b = False

#user input for c
cval = input("For c, enter 'True' or 'T' or 't' for true and 'False' or 'F' or 'f' for false: ")
#assigning boolean values to variable c depending on user input
if cval=='True' or cval=='T' or cval=='t':
    c = True
elif cval=='False' or cval=='F' or cval=='f':
    c = False

#part D
val = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
print("First part prints:", str(val))
value = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
print("Second part prints:", str(value))

#after simplification using boolean algebra
val = (not b) or ((not a) and b and (not c))
print("First part is still:", str(val))
value = ((not b) and c) or a
print("Second part is still:", str(value))

#end of program