# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB 9b ACTIVITY 2
# Date:		    26 OCTOBER 2019

#taking input for file name
name = input("Enter a file name (without the extension) in which data will be stored: ")
name = name+'.csv'
loan = open(name, 'w') #creating a new file
#taking user input
p = float(input("Enter the amount of the loan: "))
n = int(input("Enter the number of months: "))
r = float(input("Enter the annual interest rate percentage: "))
r = r/100
j = r/12
m = round(p*(j/(1-((1+j)**(-n)))),2) #monthly payment
print('The monthly payment value is: $'+str(m))
interest = 0
add = 0
intr = [0]
eb = []
bal = p
eb.append(bal)
#while ending balance is not 0
while bal>0:
    interest = round(bal * j,2) #calculating interest for each month
    add += interest
    add = round(add,2)
    intr.append(add)
    bal = round(bal-m+interest,2) #changing the value of ending balance
    eb.append(bal)
if eb[-1]<0:
    eb[-1]=0.00
loan.write("month number, interest, amount remaining \n")
#writing to the file
for i in range(len(eb)):
    loan.write(str(i)+', $'+str(intr[i])+', $'+str(eb[i])+'\n')
