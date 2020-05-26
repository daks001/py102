# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB 7b PROGRAM 3
# Date:		10 OCTOBER 2019

print("This program sorts a list and finds the median value.")
a = (input("Enter numbers separated by spaces: ")).split()
# a = [67, 78, 34, 90, 1, 6, 34, 9, -9, 23] #a hard-coded list
for i in range(len(a)):
    a[i]=int(a[i])
aa = a
a.sort() #sorting the list using python's in-built function
length = len(a)
if length%2 == 0:
    #for even number of elements in the list
    med = (a[length // 2] + a[(length // 2) - 1]) / 2
else:
    #for odd number of elements in the list
    med = a[length // 2]
print("The median value using python's sort function is:", med)
a = aa
b = [] #new list to have sorted values
m = None
mi = 0
while len(a) > 0:
    m = None
    for i in range(len(a)): #finding the minimum element in the remaining list
        if m == None: #b is empty
            m = a[i]
            mi = i
        elif m!=None and a[i] < m: #b has some elements so need to find minimum
            m = a[i]
            mi = i
    b.append(m) #adding the minimmum element to the new list
    del a[mi] #deleting the minimum element from original list 'a'
r = [] #to store the reverse of the sorted list
length = len(b)
i = length-1
while i>=0:
    r.append(b[i]) #adding last element of b in a way to make it the first element of r
    i -= 1
if length%2 == 0:
    # for even number of elements in the list
    med = (b[length // 2] + b[(length // 2) - 1]) / 2
else:
    # for odd2 number of elements in the list
    med = b[length // 2]
print("The median value using fake sort is:", med)
print("The sorted list using fake sort is:",b)
print("The reverse of the sorted list is:",r)
