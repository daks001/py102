# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
# Name:         DAKSHIKA SRIVASTAVA
# Section:      532
# Assignment:   Lab 13 Activity
# Date:         19 NOVEMBER 2019

#function 1 to find max of 3 numbers
def max_num(n1, n2, n3):
    num = [n1, n2, n3]
    return max(num)

#function 2 to find the sum of all numbers in a list
def sum_list(num):
    return sum(num)

#function 3 to multiply all numbers in a list
def pro_list(num):
    pro = 1
    for i in num:
        pro *= i
    return pro

#function 4 to reverse a string
def reverse(s):
    r = ""
    i = len(s)-1
    while i>=0:
        r += s[i]
        i -= 1
    return r

#function 5 to calculate the factorial of a non-negative number
def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f

print(max_num(1,2,3))
print(sum_list([1,2,3,4]))
print(pro_list([1,2,3,4]))
print(reverse("1234abcd"))
print(fact(3))