#Tic Tac Toe game
#board
board = []
for i in range(9):
    board.append(" ")

# if game is still on 
game_is_still_on = True

# default winner of the game
winner = None

# current player
current_player = 'X'

#display
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#play game
def play_game():

    #display the board
    display_board()

    while game_is_still_on:
        handle_turn(current_player)
        check_if_game_over()
        switch_players()

    # if the game is over ( game_is_still_on is False)
    if winner == 'X' or winner == 'O':  # check_if_win() in check_if_game_over() is True
        print(" the winner is " + winner)
    else: # check_if_tie() in check_if_game_over() is True
        print('Tie')
    
        
def handle_turn(player):
    print("it'/s ",player, ' turn')
    position = input("please choose position only 1-9 :")
    valid_position =  ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while position not in valid_position :
        position = input('Invalid position! please only choose a position from 1-9 : ')
    position = int(position)-1 
    board[position] = player
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    # set up the global variable
    global winner

    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()

    #get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    #set up the global variable
    global game_is_still_on

    # check if any row share the same value
    row_1 = board[0]==board[1]==board[2] != ' '
    row_2 = board[3]==board[4]==board[5] != ' '
    row_3 = board[6]==board[7]==board[8] != ' '
    
    # game over if there is a row winner
    if row_1 or row_2 or row_3:
        game_is_still_on = False
    
    if row_1:
        return board[0] # return the player of row 1
    elif row_2:
        return board[0] # return the player of row 2
    elif row_3:
        return board[0] # return the player of row 3
    

def check_columns():
    #set up the global variable
    global game_is_still_on
    # check if any column share the same value
    column_1 = board[0]==board[3]==board[6] != ' '
    column_2 = board[1]==board[4]==board[7] != ' '
    column_3 = board[2]==board[5]==board[8] != ' '

    #game over if there is a column winner
    if column_1 or column_2 or column_3:
        game_is_still_on = False
    
    if column_1:
        return board[0] # return the player of column 1
    elif column_2:
        return board[1] # return the player of column 2
    elif column_3:
        return board[2] # return the player of column 3
    


def check_diagonals():
    # set up the global variable
    global game_is_still_on
    # check if any diagonal share the same value
    diagonal_1 = board[0]==board[4]==board[8] != ' '
    diagonal_2 = board[2]==board[4]==board[6] != ' '
    
     # game over if there is a diagonal winner
    if diagonal_1 or diagonal_2:
        game_is_still_on = False
    
    if diagonal_1:
        return board[0] # return the player of diagonal 1
    elif diagonal_2:
        return board[2] # return the player of diagonal 2
    



def check_if_tie():
    # set up  the global variable
    global game_is_still_on
    # check if the board full
    if ' ' not in board:
        game_is_still_on = False
        return True
    else: # not tie
        return False
    

def switch_players():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'




play_game()
