# This is my first attempt to program AI 5 ziqi player
# This is attemp is finally failed as a result of the numbers of calculations
# But I havn't try the method to reduce the calculations
# I'm gonna do it in my second attemt, since that I don't want to give up on this method

import random
import socket


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

def go(currentplayer, board):
    if currentplayer == 'X':
        player_go(currentplayer,board);
    else:
        d = s.recv(1024);
        d = d.decode();
        x = int(d[:2]);
        y = int(d[2:]);
        print('other player put chess here: ',x+1,y+1);
        board[x][y] = currentplayer

def player_go(currentplayer,board):
    print("It's player:",currentplayer,"'s turn")
    row=int(input("Please input the row:"))-1
    column= int(input("Please input the column:"))-1
    while row>14 or row<0 or column>14 or column<0 or board[row][column]!="E":
        row=int(input("The psotion is invalid, please input a valid row:"))-1
        column=int(input("Please input a valid column:"))-1
    board[row][column]=currentplayer
    x = str(row);
    y = str(column);
    if len(x) == 1:
        x = '0'+x;
    if len(y) == 1:
        y = '0'+y;
    d = x+y
    s.send(d.encode());
    
    
                
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
            
def game_function():
    init()
    currentplayer="O";
    while gamefinished==False:
        go(currentplayer,board)
        output_board(board)
        checkwin(currentplayer, board)
        currentplayer=swap_player(currentplayer)

s=socket.socket();
s.connect(('172.17.134.132',9999));
print('connection established with (172.17.134.132,9999)');
game_function()
s.close();



                    
    
            
