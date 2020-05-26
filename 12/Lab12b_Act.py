# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
# Name:         DAKSHIKA SRIVASTAVA
# Section:      532
# Assignment:   Lab 12 b Activity
# Date:         17 NOVEMBER 2019

#this program will display tallies correctly, upto 100 and even more if the window is maximized

#importing turtle
from turtle import *

#function to take input
def user():
    return int(input('Enter a number: '))

n = user() #storing the input in a global variable

#calculating the number of straight lines and diagonals required
def line(n):
    l4 = (n / 4) - 1 #number of straight lines to be drawn in groups of 4
    rem = n - (l4 * 4)
    ld = l4 #number of diagonals
    rem = rem - ld
    ls = rem #number of strtaight lines remaining
    return (l4, ld, ls)

four = line(n)[0]
diag = line(n)[1]
straight = line(n)[2]

#function to draw the tallies
def draw_tallies(n):
    color('blue', 'purple')
    hideturtle()
    penup()
    #inital setup
    left(180)
    forward(600)
    right(90)
    forward(250)
    right(90)
    i = 1
    hideturtle()
    penup()
    lines = n - straight
    p = 0 #to keep track of changing lines
    #drawing the tallies
    while i<=n:
        if p % 30 == 0 and p != 0:
            #change line
            right(180)
            forward(1140)
            left(90)
            forward(150)
            left(90)
        if i % 5 == 0:
            #draw the diagonal
            left(180)
            forward(133.33)
            right(90)
            forward(100)
            right(135)
            pendown()
            showturtle()
            forward(141)
            penup()
            hideturtle()
            left(45)
            forward(90)
        else:
            #drawing the straight lines
            left(90)
            forward(100)
            right(180)
            pendown()
            showturtle()
            forward(100)
            penup()
            hideturtle()
            left(90)
            forward(33.33)
        p = i
        i += 1
    done()

#calling the function to draw
draw_tallies(n)
#end of program