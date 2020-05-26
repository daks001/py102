# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB 5b ACTIVITY c
# Date:		26 SEPTEMBER 2019

print("This program categorizes all numbers between 2 and 100 as either prime or non-prime")
c = 0 #to count the number of factors
count = 0#to count the number of prime numbers
#for loop to find factors and hence decide if a number is prime
for i in range(2,101):
    c = 0
    for j in range(1,i+1):
        if i%j == 0: #j is a factor of i
            c += 1
    if (c == 2):
        print(i,"is prime")
        count += 1
    else:
        print(i,"is not prime")
print("There are", count, "number of primes between 2 and 100.")