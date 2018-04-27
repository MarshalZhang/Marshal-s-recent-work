# This one is in charge of go

from related_move import *
from main import *


def go(currentplayer,board,related_board):
    if currentplayer=="O":
        player_go(currentplayer, board,related_board)
    else:
        AI_go(board,related_board)



def player_go(currentplayer,board,related_board):
    print("It's player:",currentplayer,"'s turn")
    row=int(input("Please input the row:"))-1
    column= int(input("Please input the column:"))-1
    while row>14 or row<0 or column>14 or column<0 or board[row][column]!="E":
        row=int(input("The psotion is invalid, please input a valid row:"))-1
        column=int(input("Please input a valid column:"))-1
    board[row][column]=currentplayer
    change_related_board(row,column,borad,related_board)
