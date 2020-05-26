# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    MAHIRAH SAMAH
#               MICHAEL MARTIN
#               JAMES GONZALEZ
# Section:		532
# Assignment:	Lab4_Activity3
# Date:		    17 SEPTEMBER 19

#part A
print("This program performs evaluations of boolean expressions")
#user input for a
aval = input("For a, enter 'True' or 'T' or 't' for true and 'False' or 'F' or 'f' for false: ")
#assigning boolean values to variable a depending on user input
if aval=='True' or aval=='T' or aval=='t':
    a = True
elif aval=='False' or aval=='F' or aval=='f':
    a = False

#part B
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

print("a and b and c is:", (a and b and c))
print("a or b or c is:", (a or b or c))

#part C
#using previous input instead of hard coding
#subpart 1
#with xor
if a^b ==True:
    print("part C subpart 1 results in True")
else:
    print("part C subpart 1 results in False")
#without xor
if (a==True or b==True) and ((a and b)==False):
    print("part C subpart 1 results in True")
else:
    print("part C subpart 1 results in False")

#subpart 2
#with xor
if a^b^c ==True:
    print("part C subpart 2 results in True")
else:
    print("part C subpart 2 results in False")
#without xor
if (((a and b and c)==True) or (((a and b and c)==False) and ((a or b or c)==True) and (((a and b)==False and (b or c)!=True) or ((b and c)==False and (a or c)!=True) or ((a and c)==False and (b or a)!=True)))):
    print("part C subpart 2 results in True")
else:
    print("part C subpart 2 results in False")

#end of program