# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:       DAKSHIKA SRIVASTAVA
#              MAHIRAH SAMAH
# Section:     532
# Assignment:  Lab14_game
# Date:        03 DECEMBER 2019


#madlibs
#number guessing game
#tic-tac-toe

import random

#to test for tic-tac-toe, if someone is winning
def test(l):
    if l[0][0]==l[0][1] and l[0][0]==l[0][2] and l[0][0]!=None:
        if l[0][0]=='x':
            return (True, 'x')
        elif l[0][0]=='o':
            return (True, 'o')
    elif l[0][0]==l[1][0] and l[0][0]==l[2][0] and l[0][0]!=None:
        if l[0][0]=='x':
            return (True, 'x')
        elif l[0][0]=='o':
            return (True, 'o')
    elif l[0][0]==l[1][1] and l[0][0]==l[2][2] and l[0][0]!=None:
        if l[0][0]=='x':
            return (True, 'x')
        elif l[0][0]=='o':
            return (True, 'o')
    elif l[0][1]==l[1][1] and l[0][1]==l[2][1] and l[0][1]!=None:
        if l[0][1]=='x':
            return (True, 'x')
        elif l[0][1]=='o':
            return (True, 'o')
    elif l[0][2]==l[1][2] and l[0][2]==l[2][2] and l[0][2]!=None:
        if l[0][2]=='x':
            return (True, 'x')
        elif l[0][2]=='o':
            return (True, 'o')
    elif l[0][2]==l[1][1] and l[0][2]==l[2][0] and l[0][2]!=None:
        if l[0][2]=='x':
            return (True, 'x')
        elif l[0][2]=='o':
            return (True, 'o')
    elif l[1][0]==l[1][1] and l[1][0]==l[1][2] and l[1][0]!=None:
        if l[1][0]=='x':
            return (True, 'x')
        elif l[1][0]=='o':
            return (True, 'o')
    elif l[2][0]==l[2][1] and l[2][0]==l[2][2] and l[2][0]!=None:
        if l[2][0]=='x':
            return (True, 'x')
        elif l[2][0]=='o':
            return (True, 'o')
    else:
        return False

#to display the tic-tac-toe board
def display(t):
    for i in range(3):
        for j in range(3):
            print(t[i][j], end='\t')
        print()

#to check if in tic-tac-toe, all cells are filled and it's a tie
def fill(t):
    if None in t:
        return True
    else:
        return False


#game's instructions
print('This game contains three mini-games: 1. Madlibs 2. Number guessing 3. Tic-tac-toe')
print('You will be repeatedly given the opportunity to enter the number corresponding to the game you want to play. Enter Q or q or quit if you want to end the game.')
choice = input('Enter 1, 2 or 3: ')

while choice != 'q' or choice != 'Q' or choice != 'quit':
    if choice == '1':
        #madlibs
        inp = {}
        # 13 inputs
        inp_var = ['colour', 'verb-ed', 'number', 'animal', 'adjective', 'tool', 'vegetable', 'container', 'fruit', 'candy', 'noun', 'furniture', 'nouns']
        #taking input for the different variables
        for i in inp_var:
            print('You will be asked to enter a ', i)
            c = input('Enter here: ')
            inp[i]=c
        print('Today we had a substitute teacher for science class, with', inp['colour'], 'hair that', inp['verb-ed'], 'straight up', inp['number'], 'inches high. His name was Mr.', inp['animal'], "and he said he'd show " \
                'us why science was the most', inp['adjective'], 'class. First, he used a', inp['tool'], 'and a', inp['vegetable'], 'to make a', inp['container'], 'of water turn', inp['colour']+ '. Then he made a', inp['noun'], 'of the solar system ' \
                'using', inp['fruit'], ',', inp['candy'], ', and', inp['noun']+ '. When the Principal walked by and saw the substitute teacher using', inp['noun'], 'to the', inp['furniture'], 'into', inp['colour'], inp['nouns'], ', she asked him to show ' \
                'the class a movie about', inp['nouns'], 'instead. The next day, we had a different substitute teacher.')
    elif choice == '2':
        #number guessing game
        i = random.randint(1,49)
        print('You will be asked to enter an integer between 1 and 50.')
        print('If your number is higher than the correct answer, you win, otherwise you lose!')
        guess = int(input('Enter here: '))
        if guess > i and guess < 51 and guess > 0:
            print('You win!!!')
        elif guess > 0 and guess < 51 and guess < i:
            print('You lose!')
        elif guess > 0 and guess < 51 and guess == i:
            print('Congratulations, you broke our system!')
        else:
            print('You rebel, next time, enter a number in range.')
    elif choice == '3':
        #tic-tac-toe
        t = [[None, None, None], [None, None, None], [None, None, None]]
        print("You will be asked to choose your symbol, and you can enter either 'x' or 'o'.")
        ch = input('Enter your choice here: ')
        cch = None
        #computer's choice is cch
        #user's choice is ch
        if ch == 'x':
            cch = 'o'
        elif ch == 'o':
            cch = 'x'
        else:
            print('You rebel, next time, follow instructions.')
            break
        display(t)
        while test(t)==False and fill(t)==False:
            r = int(input("Enter row number: "))
            c = int(input("Enter column number: "))
            #filling user's location
            if t[r][c]==None:
                t[r][c]=ch
            else:
                print('Already filled!')
            if test(t)==False:
                print('This is how it looks now:')
                display(t)
                #filling computer's location
                cr = random.randint(0,2)
                cc = random.randint(0,2)
                if t[cr][cc]==None:
                    t[cr][cc]=cch
                else:
                    while t[cr][cc]!=None:
                        cr = random.randint(0,2)
                        cc = random.randint(0,2)
                    t[cr][cc] = cch
                print("After your opponent's turn, this is how it looks:")
                display(t)
            #deciding winners, if any
            elif test(t)[1]==ch:
                print('You won!')
                break
            elif test(t)[1]==cch:
                print('You lost! Computer won.')
                break
            if fill(t)==True:
                print('There was a tie.')
                break
    elif choice== 'q' or choice == 'Q' or choice == 'quit':
        #if the user wants to quit
        break
    else:
        print('Invalid input.')
    #asking for input again
    choice = input('Enter 1 for madlibs, 2 for number guessing, 3 for tic-tac-toe, or q/Q/quit to end the game. ')

#end of program