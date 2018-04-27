# This one check win 

def checkwin(currentplayer, board):
    global gamefinished
    gamefinished=False
    if check_horizontal(currentplayer,board) or check_vertical(currentplayer, board) or check_slant(currentplayer,board):
        gamefinished =True
        print("The game has finished")
        print(currentplayer, "is the winner")
        
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
    
