# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB 5b ACTIVITY a
# Date:		26 SEPTEMBER 2019

print("This program prints Collatz Conjecture sequence upto 1")
#taking input for n
n = int(input("Enter a number: "))
count = 0 #to count the number of iterations
#while loop to calculate the consecutive terms
print(n, end=', ')
while (n>1):
    # print(n, end=', ')
    #checking if n is even or odd
    if n%2 == 0: #even
        n = n // 2
        count += 1
        print(n, end=', ')
    else: #odd
        n = (3 * n) + 1
        count += 1
        print(n, end=', ')
print("The operation took", count, "number of iterations")