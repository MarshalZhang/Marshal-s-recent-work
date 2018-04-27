# This one is in charge of the AI_move

def AI_check_four(board,related_board):
    boardcopy=board
    global row
    global column
    for i in range(15):
        for j in range(15):
            if related_board[i][j]==1:
                boardcopy[i][j]="X"
                if fake_checkwin("X",board):
                    row=i+1
                    column=j+1
                    boardcopy[i][j]="E"
                    return True
                boardcopy[i][j]="E"
                
def AI_check_opponent_four(board,related_board):
    boardcopy=board
    global row
    global column
    for i in range(15):
        for j in range(15):
            if related_board[i][j]==1:
                boardcopy[i][j]="O"
                if fake_checkwin("O",board):
                    row=i+1
                    column=j+1
                    boardcopy[i][j]="E"
                    return True
                boardcopy[i][j]="E"


def AI_check_three(board,related_board):
    boardcopy=board
    global row
    global column
    for i in range(15):
         for j in range(15):
             if boardcopy[i][j]=="E" and related_board[i][j]==1:
                 boardcopy[i][j]="X"
                 if AI_check_four(boardcopy,related_board):
                     row=i+1
                     column=j+1
                     boardcopy[i][j]="E"
                     return True
                 boardcopy[i][j]="E"

def AI_check_opponent_three(board,related_board):
    boardcopy=board
    global row
    global column
    for k in range(15):
         for w in range(15):
             if boardcopy[k][w]=="E" and related_board[k][w]==1:
                 boardcopy[k][w]="O"
                 related_board=get_related_board(board)
                 for x in range(15):
                     for y in range(15):
                         if boardcopy[x][y]=="E" and related_board[x][y]==1:
                             boardcopy[x][y]="X"
                             related_board=get_related_board(board)
                             if AI_check_opponent_four(boardcopy,related_board):
                                 row=k+1
                                 column=w+1
                                 boardcopy[k][w]="E"
                                 boardcopy[x][y]="E"
                                 return True
                             boardcopy[x][y]="E"
                 boardcopy[k][w]="E"



                 
def AI_random(board,related_board):
    global row
    global column
    row=random.randint(1,15)
    column=random.randint(1,15)
    while board[row-1][column-1]!="E" or related_board[row-1][column-1]==0:
        row=random.randint(1,15)
        column=random.randint(1,15)
        
    

def AI_go(board,related_board):
    if AI_check_four(board,related_board):
        output_AI_move(row,column,board)
        
    elif AI_check_opponent_four(board,related_board):
        print("aha, I won't let you win5")
        output_AI_move(row, column,board)
        
    elif AI_check_three(board,related_board):
        print("aha, You're gonna let me win")
        output_AI_move(row,column, borad)

    elif AI_check_opponent_three(board,related_board):
        print("Defence, I won't let you connet 4")
        output_AI_move(row,column,board)
    else:
        AI_random(board,related_board)
        output_AI_move(row, column,board)

def output_AI_move(row, column,board):
    print("It's AI's turn,please choose row:",row)
    print("Please choose column:",column)
    board[row-1][column-1]="X"
