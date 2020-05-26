# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	Lab 11b Activity 1(b)
# Date:		    8 NOVEMBER 2019

#creating a function to return the name and net profitability of the least profitable facility
def profit(name,cost,value):
    prof = {}
    minp = None #minimum profit
    mini = None #index of minimum profit
    c = 0
    #making a dictionary of form {name:profit_value}
    for i in range(len(cost)):
        prof[name[i]] = value[i]-cost[i]
    #finding the minimum profit value
    for key in prof.values():
        if minp == None:
            minp = key
            mini = c
        elif minp > key:
            minp = key
            mini = c
        c += 1
    minn = name[mini]
    return (minn+' '+str(minp))
#taking input
name = (input('Enter the name of the facility: ')).split()
cost = (input('Enter the cost of operation: ')).split()
for i in range(len(cost)):
    cost[i] = float(cost[i])
value = (input('Enter the value of the products: ')).split()
for i in range(len(value)):
    value[i] = float(value[i])
#calling the function
print(profit(name, cost, value))
