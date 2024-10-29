import numpy as np
import random

board=np.full((3,3)," ")

def display_boart():
    print("\n  0   1   2 ")
    print(" ┌───┬───┬───┐")
    for i, row in enumerate(board):
        print(f"{i}│ {' │ '.join(row)} │")
        if i < 2:
            print(" ├───┼───┼───┤")
    print(" └───┴───┴───┘\n")


def check_win(player):
    for i in range(3):
        if all([cell==player for cell in board[i,:]]) or all ([cell==player for cell in board[:,i]]):
            return True
        if board[0,0]==board[1,1]==board[2,2]==player:
            return True
    return False


def check_draw():
    return not any (cell==" " for row in board for cell in row)


def make_move(player):
    while True:
        try:
            row=int(input(f"player{player}, enter row(0,1,2)"))
            col=int(input(f"player{player},enter col(0,1,2)"))
            if board[row,col]==' ':
                board[row,col]=player
                break
            else:
                print("place already taken")
        except(ValueError,IndexError):
            print("invalid input try again")

def cpu_move():
    empty_cells=[(i,j) for i in range(3) for j in range(3) if board[i,j]==" "]
    if empty_cells:
        row,col=random.choice(empty_cells)
        board[row,col]='O'
        


#main game 

def tic_tac_toe():
    mode=input("Enter '1' to play against CPU,or '2' if you want to play 2 players: ")
    while mode!='1' and mode!='2':
        print("invalid options")
        mode=input("Enter '1' to play against CPU,or '2' if you want to play 2 players: ")
        
    c_player='X'
    while True:
        display_boart()
        if c_player=='X':
            make_move(c_player)
        else:
            if mode=='1':
                cpu_move()
            else:
                make_move(c_player)

        if check_win(c_player):
            display_boart()
            print()
            
            print(f"player {c_player} wins!")
            break
        elif check_draw():
            display_boart()
            print()
            print("its a draw")
            break

        c_player="O" if c_player=='X' else 'X'


tic_tac_toe()
