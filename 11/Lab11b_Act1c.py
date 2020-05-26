# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	Lab 11b Activity 1(c)
# Date:		    8 NOVEMBER 2019

#creating a function to return user info as a mailing label
def mail():
    #taking input
    name = input('Enter your name: ')
    city = input('Enter your city: ')
    state = input('Enter your state: ')
    zipc = input('Enter your zip code: ')
    address = input('Enter your address: ')
    print(name)
    print(address)
    print(city, state, zipc)
#calling the function
mail()