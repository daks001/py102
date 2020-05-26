# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    MAHIRAH SAMAH
#               MICHAEL MARTIN
# Section:		532
# Assignment:	Lab7_Activity2
# Date:		    8 OCTOBER 19

gradeData=[79,99,73,49,67,62,52,99,57,58,67,88,71,69,41,74,53,90,63,66,92,54,61,59,48,71, \
           83,89,99,69,66,40,48,41,99,68,52,78,77,71,40,65,77,87,96,44,54,60,89,72] #sample data
#part A
sum = 0
for i in gradeData:
    sum+=i #sum of all elements in the list
mean = sum/(len(gradeData)) #mean of the list elements
add = sum #storing the value of sum for part D
print('The mean of the grades is:', mean)

#part B
sum = 0
for i in gradeData:
    sum += (i-mean)**2
sd = (sum/(len(gradeData)))**0.5 #standard deviation of the list elements
print(sd)

#part C
min_num = None
max_num = None
for i in gradeData:
    if min_num==None: #for no minimum value
        min_num = i
    elif min_num!=None and min_num>i: #for a smaller value than min_num
        min_num = i

    if max_num==None: #for no maximum value
        max_num=i
    elif max_num!=None and max_num<i: #for a larger value than max_num
        max_num=i

print("The minimum value is", min_num)
print("The maximum value is", max_num)

#part D
avg = 75.0
l = len(gradeData) #number of elements in the list
deltaGrade = (avg*l - add) / l #calculating deltaGrade
print('The minimum value to be added to each grade is:',deltaGrade)