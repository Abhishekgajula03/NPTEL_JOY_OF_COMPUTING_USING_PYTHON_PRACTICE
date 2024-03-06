import numpy


def play():
    for turns in range(9):
        if turns%2==0:
            print("it is X turn")
            place(p1)
            if won(p1):
                break
        else:
            print("it is X turn")
            place(p2)
            if won(p2):
                break
def place(symbol):
    print(numpy.matrix(board))#it will take the board in list format convert it in row and col format
    while(1):
        row=int(input("choose x from 1 2 3: "))   
        col=int(input("choose o from 1 2 3: "))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=="_":
            break
    board[row-1][col-1]=symbol# if this kept inside the while loop the game won get updated
def won(symbol):
    return check_row(symbol) or check_col(symbol) or check_diagonal(symbol)
def check_row(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if (board[r][c]==symbol):
                count=count+1
        if count==3:
            print(symbol,"won")
            return True
        return False
def check_col(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if (board[r][c]==symbol):
                count=count+1
        if count==3:
            print(symbol,"won")
            return True
        return False
def check_diagonal(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol,'won')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        print(symbol,'won')
        return True
    return False
board=numpy.array([['_','_','_'],['_','_','_'],['_','_','_']])
p1='X'
p2='O'
play()
