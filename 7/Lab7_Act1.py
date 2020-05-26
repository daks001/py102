# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    MAHIRAH SAMAH
#               MICHAEL MARTIN
# Section:		532
# Assignment:	Lab7_Activity1
# Date:		    8 OCTOBER 19

#part 1
inp = input("Enter 3 or more stock prices separated by commas: ")
elements = inp.split() #storing the different prices entered
price = [] #empty list
for i in elements:
    price.append(i) #adding each price as an element of the list

for i in price:
    print('$'+i, end=' ') #printing the desired output

#part 2
# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers:')
tokens = user_input.split()  # Split into separate strings
# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))
# Print each position and number print() # Print a single newline
for index in range(len(nums)):
    value = nums[index]
    print('%d: %d' % (index, value))
# Determine minimum odd number
min_num = None
for num in nums:
    if (min_num == None) and (num % 2 != 0): # First odd number found
        min_num = num
    elif (min_num != None) and (num < min_num ) and (num % 2 != 0): # Larger odd number found
        min_num = num
print('Min odd #:', min_num)

#part 3
temp = [75.5, 80.1, 85.9, 90, 95.6] #hardcoded list of temperature values
sep = input("Enter a two character string to serve as a separator: ") #taking input for separator
for i in temp:
    if i != temp[-1]: #for every element except the last one
        print(i,sep, end=' ')
    else: #for the last element
        print(i,'\n')
