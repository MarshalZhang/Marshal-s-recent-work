def try_related(i,j,related_board):
    try:
        related_board[i][j]=1
    except IndexError:
        pass
    if board[i][j]!="E":
        pass
    

def change_related_board(row,column,borad,related_board):
    i=row-1
    j=column-1
    try_related(i,j-1,related_board)
    try_related(i,j+1,related_board)
    try_related(i-1,j-1,related_board)
    try_related(i-1,j,related_board)
    try_related(i-1,j+1,related_board)
    try_related(i+1,j-1,related_board)
    try_related(i+1,j,related_board)
    try_related(i+1,j+1,related_board)
    for k in range(i-1,i+2):
        for w in range(j-1,j+2):
            if board[k][w]!="E":
                related_board[k][w]=0
    related_board[i][j]=0
    return related_board
    
    

def get_related_board(board):
    related_board=[[0 for i in range(15)]for j in range(15)]
    for i in range(15):
        for j in range(15):
            if board[i][j]!="E":
                try_related(i,j-1,related_board)
                try_related(i,j,related_board)
                try_related(i,j+1,related_board)
                try_related(i-1,j-1,related_board)
                try_related(i-1,j,related_board)
                try_related(i-1,j+1,related_board)
                try_related(i+1,j-1,related_board)
                try_related(i+1,j,related_board)
                try_related(i+1,j+1,related_board)
    for i in range(15):
        for j in range(15):
            if board[i][j]!="E":
                related_board[i][j]=0
    return related_board

def output_related_board(related_board):
    for i in range(15):
        for j in range(15):
            print(related_board[i][j], end=" ")
        print()
    
                
