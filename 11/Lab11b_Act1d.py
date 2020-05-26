# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	Lab 11b Activity 1(d)
# Date:		    8 NOVEMBER 2019

#creating a function to convert .csv data to .tsv
def ct(filename):
    content = []
    #opening the file to be read
    with open(filename, 'r') as data:
        for i in data:
            #extracting th info in data
            content.append(i.split(','))
    #creating a new file .tsv
    with open('New File.tsv','w') as ndata:
        for i in content:
            #writing data to ndata
            for j in i:
                ndata.write(j+'\t')
            ndata.write('\n')

#calling the function by taking input
file = input('Enter file name, followed by the extension .csv: ')
ct(file)