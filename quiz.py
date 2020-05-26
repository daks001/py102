# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	QUIZ
# Date:		    17 SEPTEMBER 2019

print("This program calculates the total cost of coffee")
#inputting amount of coffee in pounds
amt_of_coffee = float(input("Enter the amount of coffee to be shipped in pounds: "))
#assigning price values (for one pound) to variables
cost_of_coffee = 10.50
cost_of_shipping = 0.86
flat_fee = 1.50
#calculating total cost of coffee
total_cost_of_coffee = amt_of_coffee * cost_of_coffee
total_cost_of_shipping = amt_of_coffee * cost_of_shipping
total_cost = total_cost_of_coffee + total_cost_of_shipping + flat_fee

print("The total cost of the order is:", total_cost)

