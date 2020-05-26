# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		DAKSHIKA SRIVASTAVA
# Section:		532
# Assignment:	LAB 7b PROGRAM 1
# Date:		10 OCTOBER 2019

print("This program converts a word in Pig Latin.")
inp=input("Enter a word or 'stop' to stop: ")
a=0
i=0
c=''
r=''
while inp!='stop' or inp!='STOP' or inp!='Stop':
    if inp=='stop' or inp=='Stop' or inp=='STOP': #program should terminate
        break
    else:
        #reinitialising variables
        i=0
        c=''
        r=''
        if inp[0]!='a' and inp[0]!='e' and inp[0]!='i' and inp[0]!='o' and inp[0]!='u' and inp[0]!='y' and inp[0]!='A' and inp[0]!='E' and inp[0]!='I' and inp[0]!='O' and inp[0]!='U' and inp[0]!='Y':
           #first character is a consonant
            while inp[0]!='a' and inp[0]!='e' and inp[0]!='i' and inp[0]!='o' and inp[0]!='u' and inp[0]!='y' and inp[0]!='A' and inp[0]!='E' and inp[0]!='I' and inp[0]!='O' and inp[0]!='U' and inp[0]!='Y':
                c=c+inp[i] #concatenating all consonants into a string
                i+=1
                if i==len(inp) or inp[i]=='a' or inp[i]=='e' or inp[i]=='i' or inp[i]=='o' or inp[i]=='u' or inp[i]=='y' or inp[i]=='A' or inp[i]=='E' or inp[i]=='I' or inp[i]=='O' or inp[i]=='U' or inp[i]=='Y':
                    break #if a vowel is found or i exceeds string index
            for j in range(i,len(inp)):
                r=r+inp[j] #concatenating all characters following the vowels into a string
            r=r+c+'ay' #storing the final output
            print(r)
        else: #starts with vowel
            print(inp+'yay')
    inp = input("Enter a word or 'stop' to stop: ")
