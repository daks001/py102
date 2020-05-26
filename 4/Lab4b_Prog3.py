# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    MAHIRAH SAMAH
#               MICHAEL MARTIN
# Section:		532
# Assignment:	Lab4b_Program3
# Date:		    19 SEPTEMBER 19

print("This program calculates the total number of widgets produced from the initial testing phase up to and including the day entered")
print("Valid range for the number of days is 1 to 100, both limits inclusive. Please enter a day number within this range.")
#taking input for the day number
day = int(input("Enter here: "))
widget = 0
days = day
#using relational operators to find the total number of widgets produced
if day<=100: #if day number is valid
    if day<=10:
        widget = 10*day
    elif day>10 and day<=60:
        widget = 10*10
        day = day-10
        widget += day*40
    elif day>60 and day<=100:
        widget = 10*10 + 40*50
        set = 39
        day = day-60
        while day>=1:
            widget += set
            set -= 1
            day -= 1
    print("The number of widgets produced after", days, "days is:", widget)
else: #day number is invalid
    print("Invalid input for day")

#end of program