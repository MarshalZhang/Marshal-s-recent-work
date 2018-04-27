# This is my first attempt to program AI 5 ziqi player
# This is attemp is finally failed as a result of the numbers of calculations
# But I havn't try the method to reduce the calculations
# I'm gonna do it in my second attemt, since that I don't want to give up on this method

import random



def init():
    global board
    global gamefinished
    board=[["E" for i in range(15)]for j in range(15)]
    playerwon=None
    currentplayer="O"
    gamefinished=False
                

def output_board(board):
    for i in range(15):
        for j in range(15):
            print(board[i][j], end=" ")
        print()

def go(currentplayer, board, AI_active):
    if AI_active==False:
        player_go(currentplayer, board)
    if AI_active==True:
        if currentplayer=="O":
            player_go(currentplayer, board)
        else:
            AI_go(board)



def player_go(currentplayer,board):
    print("It's player:",currentplayer,"'s turn")
    row=int(input("Please input the row:"))-1
    column= int(input("Please input the column:"))-1
    while row>14 or row<0 or column>14 or column<0 or board[row][column]!="E":
        row=int(input("The psotion is invalid, please input a valid row:"))-1
        column=int(input("Please input a valid column:"))-1
    board[row][column]=currentplayer
        
                   
                
def check_horizontal(currentplayer,board):
    f=1
    for i in range(11):
        for j in range(15):
            for k in range(i,i+5):
                if board[k][j]==currentplayer:
                    f*=1
                else:
                    f*=0
            if f==1:
                return True
            f = 1
        
                    

def check_vertical(currentplayer, board):
    f=1
    for i in range(15):
        for j in range(11):
            for k in range(j,j+5):
                if board[i][k]==currentplayer:
                    f*=1
                else:
                    f*=0
            if f==1:
                return True
            f = 1
                
                    
      
def check_slant(currentplayer,board):
    if check_major_diagonal(currentplayer, board) or check_minor_diagonal(currentplayer, board):
        return True

def check_major_diagonal(currentplayer, board):
    f=1
    for i in range(11):
        for j in range(11):
            for k in range(i,i+5):
                d=k-i                    # this is the difference between k and i
                if board[k][j+d]==currentplayer:
                    f*=1
                else:
                    f*=0
            if f==1:
                return True
            f=1
            
def check_minor_diagonal(currentplayer, board):
    f=1
    for i in range(11):
        for j in range(5,15):
            for k in range(i,i+5):
                d=k-i                    # this is the difference between k and i
                if board[k][j-d]==currentplayer:
                    f*=1
                else:
                    f*=0
            if f==1:
                return True
            f=1
    
    

def checkwin(currentplayer, board):
    global gamefinished
    gamefinished=False
    if check_horizontal(currentplayer,board) or check_vertical(currentplayer, board) or check_slant(currentplayer,board):
        gamefinished =True
        print("The game has finished")
        print(currentplayer, "is the winner")
    

def fake_checkwin(currentplayer, board):
    if check_horizontal(currentplayer,board) or check_vertical(currentplayer, board) or check_slant(currentplayer,board):
        return True
    else:
        return False
    
    

def swap_player(currentplayer):
    if currentplayer=="O":
        currentplayer="X"
    else:
        currentplayer="O"
    return currentplayer

def AI_check_four(board):
    boardcopy=board
    global row
    global column
    for i in range(15):
        for j in range(15):
            if boardcopy[i][j]=="E":
                boardcopy[i][j]="X"
                if fake_checkwin("X",board):
                    row=i+1
                    column=j+1
                    boardcopy[i][j]="E"
                    return True
                boardcopy[i][j]="E"
                
def AI_check_opponent_four(board):
    boardcopy=board
    global row
    global column
    for i in range(15):
        for j in range(15):
            if boardcopy[i][j]=="E":
                boardcopy[i][j]="O"
                if fake_checkwin("O",board):
                    row=i+1
                    column=j+1
                    boardcopy[i][j]="E"
                    return True
                boardcopy[i][j]="E"

def AI_check_three(board):
    boardcopy=board
    global row
    global column
    for i in range(15):
         for j in range(15):
             if boardcopy[i][j]=="E":
                 boardcopy[i][j]="X"
                 if AI_check_four(boardcopy):
                     row=i+1
                     column=j+1
                     boardcopy[i][j]="E"
                     return True
                 boardcopy[i][j]="E"

def AI_check_opponent_three(board):
    boardcopy=board
    global row
    global column
    for k in range(15):
         for w in range(15):
             if boardcopy[k][w]=="E":
                 boardcopy[k][w]="O"
                 for x in range(15):
                     for y in range(15):
                         if boardcopy[x][y]=="E":
                             boardcopy[x][y]="X"
                             if AI_check_opponent_four(boardcopy):
                                 row=k+1
                                 column=w+1
                                 boardcopy[k][w]="E"
                                 boardcopy[x][y]="E"
                                 return True
                             boardcopy[k][w]="E"
                         boardcopy[x][y]="E"
                 
def AI_random(board):
    global row
    global column
    row=random.randint(1,15)
    column=random.randint(1,15)
    while board[row-1][column-1]!="E":
        row=random.randint(1,15)
        column=random.randint(1,15)
        
    

def AI_go(board):
    if AI_check_four(board):
        output_AI_move(row,column,board)
        
    elif AI_check_opponent_four(board):
        print("aha, I won't let you win5")
        output_AI_move(row, column,board)

    elif AI_check_three(board):
        print("aha, You're gonna let me win")
        output_AI_move(row,column, borad)

    elif AI_check_opponent_three(board):
        print("Aha, I won't let you win4")
        output_AI_move(row,column,board)

    else:
        AI_random(board)
        output_AI_move(row, column,board)

def output_AI_move(row, column,board):
    print("It's AI's turn,please choose row:",row)
    print("Please choose column:",column)
    board[row-1][column-1]="X"
    

def Choose_player():
    global AI_active
    option=int(input("Please choose between one player or two players(1/2):"))
    if option==1:
        AI_active=True
    if option==2:
        AI_active=False
            
def game_function():
    init()
    currentplayer="O"
    Choose_player()
    while gamefinished==False:
        go(currentplayer,board,AI_active)
        output_board(board)
        checkwin(currentplayer, board)
        currentplayer=swap_player(currentplayer)

game_function()

                    
    
            
