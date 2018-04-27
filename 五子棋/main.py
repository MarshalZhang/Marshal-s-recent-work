# This is my second attempt to do the AI recurssion step
# In this attempt,I create another board called related_board to see if some position
# is within two step away from the not empty space
# In this attempt, I remove the option to choose two players, which means that
# This one is only focused on AI

from  random import *
from check_win import *
from AI_move import *
from go import *
from  related_move import *

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
    currentplayer="O"
    related_board=[[0 for i in range(15)]for j in range(15)]
    
    while gamefinished==False:
        go(currentplayer,board,related_board)
        output_board(board)
        checkwin(currentplayer, board)
        currentplayer=swap_player(currentplayer)

game_function()
