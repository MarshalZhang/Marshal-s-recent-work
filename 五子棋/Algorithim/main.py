


import random    



def player_go(board):
    i=int(input("It's your turn, please choose the row number:"))-1
    j=int(input("Please choose the column number:"))-1
    while i<0 or i>14 or j<0 or j>14 or board[i][j]!="E":
        print("The value is invalid, please input again")
        i=int(input("It's your turn, please choose the row number:"))-1
        j=int(input("Please choose the column number:"))-1
    board[i][j]="O"

def Extent_board(board):
    extent_board=[['E' for i in range(23)]for j in range(23)]
    for i in range(15):
        for j in range(15):
            extent_board[i+4][j+4]=board[i][j]
    return extent_board

def horizontal(board,i,j,player,n):
    extent_board=Extent_board(board)
    extent_board[i+4][j+4]=player
    f=1
    for k in range(5):
        for x in range(j-k, j-k+5):
            if extent_board[i+4][x+4]==player:
                f*=1
            else:
                f*=0
        if f==1:
            extent_board[i+4][j+4]="E"
            return True
    extent_board[i+4][j+4]="E"

def vertical(board,i,j,player,n):
    extent_board=Extent_board(board)
    extent_board[i+4][j+4]=player
    f=1
    for k in range(n):
        for x in range(i-k,i-k+n):
            if extent_board[x+4][j+4]==player:
                f*=1
            else:
                f*=0
        if f==1:
            extent_board[i+4][j+4]="E"
            return True
    extent_board[i+4][j+4]="E"

def Major_Diagonal(board,i,j,player,n):
    extent_board=Extent_board(board)
    extent_board[i+4][j+4]=player
    f=1
    for k in range(n):
        for x in range(i-k,i-k+n):
                if extent_board[x+4][j-k+n+4]==player:
                    f*=1
                else:
                    f*=0
        if f==1:
            extent_board[i+4][j+4]="E"
            return True
    extent_board[i+4][j+4]="E"

def Minor_Diagonal(board,i,j,player,n):
    extent_board=Extent_board(board)
    extent_board[i+4][j+4]=player
    f=1
    for k in range(n):
        for x in range(i-k,i-k+n):
                if extent_board[x+4][j+k-n+4]==player:
                    f*=1
                else:
                    f*=0
    extent_board[i+4][j+4]="E"
    if f==1:
        return True

def helper(board,i,j,player,n):    
    my_weight_dict=[2,8,18,100,1000]#parameter should be changed later in this array
    opponent_weight_dict=[1,4,12,30,500]
    x=0
    if player=="X":
        if horizontal(board,i,j,player,n):
            x+=my_weight_dict[n-1]
        if vertical(board,i,j,player,n):
            x+=my_weight_dict[n-1]
        if Major_Diagonal(board,i,j,player,n):
            x+=my_weight_dict[n-1]
        if Minor_Diagonal(board,i,j,player,n):
            x+=my_weight_dict[n-1]
    else:
        if horizontal(board,i,j,player,n):
            x+=opponent_weight_dict[n-1]
        if vertical(board,i,j,player,n):
            x+=opponent_weight_dict[n-1]
        if Major_Diagonal(board,i,j,player,n):
            x+=opponent_weight_dict[n-1]
        if Minor_Diagonal(board,i,j,player,n):
            x+=opponent_weight_dict[n-1]
    return x
        
        
def My_weight(board,i,j):
    x=0
    for n in range(1,6):
        x+=helper(board,i,j,"X",n)
    return x
    

def Opponent_weight(board,i,j):
    x=0
    for n in range(1,6):
        x+=helper(board,i,j,"O",n)
    return x

                  

def Weight_board(board): # return a borad with weight on it
    weight_board=[[0 for i in range(15)] for j in range(15)]
    for i in range(15):
        for j in range(15):
            if board[i][j]!="E":
                weight_board[i][j]=0
            else:
                weight_board[i][j]=My_weight(board,i,j)+Opponent_weight(board,i,j)

    return weight_board

def AI_go(board):
    maxi=0
    maxj=0
    weight_board= Weight_board(board)
    for i in range(15):
        for j in range(15):
            if weight_board[i][j]>weight_board[maxi][maxj]:
                maxi=i
                maxj=j
    board[maxi][maxj]="X"
            
            



def check_horizontal(currentpalyer,board):
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

def output_board(board):
    for i in range(15):
        for j in range(15):
            print(board[i][j], end=" ")
        print()

def go(currentplayer, board):
    if currentplayer=="O":
        player_go(board)
    else:
        AI_go(board)

def swap_player(currentplayer):
    if currentplayer=="O":
        currentplayer="X"
    else:
        currentplayer="O"
    return currentplayer
    
def main():
    board=[["E" for i in range(15)] for j in range(15)]
    global currentplayer
    currentplayer="O"
    gamefinished=False
    while gamefinished==False:
        go(currentplayer,board)
        output_board(board)
        checkwin(currentplayer, board)
        currentplayer=swap_player(currentplayer)

main()


    



    
