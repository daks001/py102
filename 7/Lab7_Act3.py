# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    MAHIRAH SAMAH
#               MICHAEL MARTIN
# Section:		532
# Assignment:	Lab7_Activity3
# Date:		    8 OCTOBER 19

#making a 2D array for the chessboard
board = [['R','N','B','Q','K','B','N','R'] , \
         ['P','P','P','P','P','P','P','P'] , \
         ['.','.','.','.','.','.','.','.'] , \
         ['.','.','.','.','.','.','.','.'] , \
         ['.','.','.','.','.','.','.','.'] , \
         ['.','.','.','.','.','.','.','.'] , \
         ['p','p','p','p','p','p','p','p'] , \
         ['r','n','b','q','k','b','n','r']]

inp=input("Enter 'yes' to play or 'no' to terminate: ")
pi = 0
pj = 0
while inp=='yes':
    #while the user wants to play
    print("This is what the board looks like:")
    #printing out the chessboard
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=' ')
        print()
    #taking input for the user's move
    piece = input("Enter the piece you want to move. Enter in lower case if it's white and upper case if it's black: ")
    pi = int(input("Enter the row this piece is in: "))
    pj = int(input("Enter the column this piece is in: "))

    if piece==board[pi][pj]:
        #correct location
        dr = input("Enter +1 if the piece has to go to the right, -1 if to the left or 0 for no horizontal move: ")
        if dr!='0':
            mr = int(input('Enter the number of moves you want to make horizontally: '))
        dc = input("Enter +1 if the piece has to go up, -1 if down or 0 for no vertical move: ")
        if dc!='0':
            mc = int(input('Enter the number of moves you want to make vertically: '))
        if dr=='+1':
            #right move
            if pj+mr>7:
                print('Error. Number of moves exceeds the limit of the board.')
            else:
                if dc == '+1':
                    # upward move
                    if pi - mc < 0:
                        print("Error. Number of moves exceeds the limit of the board.")
                    else:
                        board[pi - mc][pj+mr] = piece #changing location of the piece
                        board[pi][pj] = '.' #making the previous location empty
                elif dc == '-1':
                    # downward move
                    if pi + mc > 7:
                        print("Error. Number of moves exceeds the limit of the board.")
                    else:
                        board[pi + mc][pj+mr] = piece #changing location of the piece
                        board[pi][pj] = '.' #making the previous location empty
                elif dc == '0':
                    board[pi][pj] = board[pi][pj]
                else:
                    print("Invalid input.")
        elif dr=='-1':
            #left move
            if pj-mr<0:
                print('Error. Number of moves exceeds the limit of the board.')
            else:
                if dc == '+1':
                    # upward move
                    if pi - mc < 0:
                        print("Error. Number of moves exceeds the limit of the board.")
                    else:
                        board[pi - mc][pj-mr] = piece #changing location of the piece
                        board[pi][pj] = '.' #making the previous location empty
                elif dc == '-1':
                    # downward move
                    if pi + mc > 7:
                        print("Error. Number of moves exceeds the limit of the board.")
                    else:
                        board[pi + mc][pj-mr] = piece #changing location of the piece
                        board[pi][pj] = '.' #making the previous location empty
                elif dc == '0':
                    board[pi][pj] = board[pi][pj]
                else:
                    print("Invalid input.")
        elif dr=='0':
            if dc == '+1':
                # upward move
                if pi - mc < 0:
                    print("Error. Number of moves exceeds the limit of the board.")
                else:
                    board[pi - mc][pj] = piece #changing location of the piece
                    board[pi][pj] = '.' #making the previous location empty
            elif dc == '-1':
                # downward move
                if pi + mc > 7:
                    print("Error. Number of moves exceeds the limit of the board.")
                else:
                    board[pi + mc][pj] = piece #changing location of the piece
                    board[pi][pj] = '.' #making the previous location empty
            elif dc == '0':
                board[pi][pj] = board[pi][pj]
            else:
                print("Invalid input.")
        else:
            print("Invalid input.")

        print("This is what the board looks like:")
        for i in range(8):
            for j in range(8):
                print(board[i][j], end=' ')
            print()
    else:
        print("Invalid input for location.")
    inp = input("Enter 'yes' to play or 'no' to terminate: ")

