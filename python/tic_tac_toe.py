# Global Variables
board         = ['-', '-', '-',
                 '-', '-', '-',
                 '-', '-', '-']

PLAYER_1      = input('Enter Player 1 Name:')
PLAYER_2      = input('Enter Player 2 Name:')
# TODO : Check the PLAYER_1 and PLAYER_2 name is (A-Z) or (a-z)
game_not_over = True
winner        = None
player        = PLAYER_1
last_player   = 'None'

def tic_tac_toe():

    # Display Initial Board
    display_board()    

    while game_not_over:
          global player
          handle_turn(player)
          check_game_over()
          change_player()

    if winner == PLAYER_1 or winner == PLAYER_2:
        print('Game won by ' + winner + '.')     
    elif winner == None:
        print('Game draw.')    

def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])        
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])        
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])        

def handle_turn(player):
    global last_player
    valid  = False

    print(player + '\'s' + ' turn')
    position = input('Choose a position from 1-9: ')

    while not valid:
      while position not in ['1', '2', '3', 
                             '4', '5', '6', 
                             '7', '8', '9']:
         position = input('Invalid input, Choose a position only from 1-9: ')
        
      position = int(position) - 1

      if board[position] == '-':
         valid = True
      else:   
         print('Already the position was taken by',last_player)

    last_player     = player
    board[position] = player
    display_board()    

def check_game_over():
    check_for_win()
    check_for_draw()

def check_for_win():
    global winner # To access global variables (value changed inside this function)
    row_winner      = row_hit()
    column_winner   = column_hit()
    diagonal_winner = diagonal_hit()
    if row_winner:
       winner = row_winner
    elif column_winner:
       winner = column_winner
    elif diagonal_winner:
       winner = diagonal_winner
    else:
       winner = None
    return

def check_for_draw():
    global game_not_over
    if '-' not in board:
       game_not_over  = False
    return

def row_hit():
    global game_not_over
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    if row_1 or row_2 or row_3:
       game_not_over = False  

    if row_1:
       return board[0]
    elif row_2:
       return board[3]
    elif row_3:
       return board[6]
    return

def column_hit():
    global game_not_over
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    if column_1 or column_2 or column_3:
       game_not_over = False  

    if column_1:
       return board[0]
    elif column_2:
       return board[1]
    elif column_3:
       return board[2]
    return

def diagonal_hit():
    global game_not_over
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[2] == board[4] == board[6] != '-'

    if diagonal_1 or diagonal_2:
       game_not_over = False  

    if diagonal_1 or diagonal_2:
       return board[4]
    return

def change_player():
    global player
    if player == PLAYER_1:
       player = PLAYER_2
    elif player == PLAYER_2:
       player = PLAYER_1
    return

def check_player_name(PLAYER_1, PLAYER_2):
      # player_pick = False

      # while not player_pick:
      #    if (PLAYER_1 == '[A-Za-z]') and (PLAYER_2 == '[A-Za-z]'):  
      #       player_pick = True
      #    else:
      #       PLAYER_1 = input('Enter Player 1 Name:')
      #       PLAYER_2 = input('Enter Player 2 Name:')

      # Main Program call
      tic_tac_toe()

check_player_name(PLAYER_1, PLAYER_2)
