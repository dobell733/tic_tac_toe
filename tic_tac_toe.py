import random

def display_board(board):
    print('\n'*100)
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')

def player_input():
    player_symbol = ''
    
    while not(player_symbol == 'X' or player_symbol == 'O'):
        player_symbol = input('Please pick X or O ').upper()
            
        if player_symbol != 'X' or player_symbol != 'O':
            print('\n'*100)
            print('Please pick X or O ')
            print('\n'*100)
                
    if player_symbol == 'X':
        print('\n'*100)
        return ('X', 'O')
    elif player_symbol == 'O':
        print('\n'*100)
        return ('O', 'X')
        

def place_marker(board, marker, position):
    board[position] = marker

#Checks if any win conditions have been met, returns True if player has won
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark)or
    (board[4] == mark and board[5] == mark and board[6] == mark)or
    (board[1] == mark and board[2] == mark and board[3] == mark)or
    (board[7] == mark and board[4] == mark and board[1] == mark)or
    (board[8] == mark and board[5] == mark and board[2] == mark)or
    (board[9] == mark and board[6] == mark and board[3] == mark)or
    (board[7] == mark and board[5] == mark and board[3] == mark)or
    (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first():
    first = random.randint(1,2)
    
    if first == 1:
        return 'Player 1'
    else:
        return 'Player 2'

#Checks if there is a space at a given position on the board, returns True if there is, returns false if there is not a space
def space_check(board, position):
    return board[position] == ' '

#Checks every space on the board and returns False if board isn't full, and True if board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    else:
        return True

# Asks user for number 1-9 and returns number as position as long as the space isn't taken
def player_choice(board):
    position = 0
    
    while position not in range(1,10) and not space_check(board, position):
        position = int(input('Please pick a number 1-9 (spaces on board correspond to numpad layout on keyboard) '))
            
        if position not in range(1,10) and not space_check(board, position):
            print('\n'*100)
            print('Please pick a number between 1-9 or a space that is not already taken ')
                
    return position

def replay():
    play_again = ''
    
    while not(play_again == 'Y' or play_again == 'N'):
        play_again = input('Would you like to play again? Y or N ').upper()
            
        if play_again != 'Y' or play_again != 'N':
            print('\n'*100)
            print('Please pick Y or N ')
            print('\n'*100)
                
    if play_again == 'Y':
        return True
    else:
        return False

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    theBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    
    print(turn + ' will go first')

    play_game = input('Are you ready to play? Enter Y or N.').upper()
    
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        #Player 1 Turn
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker , position)
            
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 1 has won the game!')
                break
            else:
                if full_board_check(theBoard):
                   display_board(theBoard)
                   print('This game is a draw :/')
                   break
                else:
                    turn = 'Player 2'
        # Player2's turn.
        else: 
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker , position)
            
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Player 1 has won the game!')
                break
            else:
                if full_board_check(theBoard):
                   display_board(theBoard)
                   print('This game is a draw :/')
                   break
                else:
                    turn = 'Player 1'
    if not replay():
        break

    