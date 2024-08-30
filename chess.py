#white is uppercase, black is lowercase
pieces = {
    'P': 1, 'R': 5, 'N': 3, 'B': 3, 'Q': 9, 'K': float('inf'),  
    'p': 1, 'r': 5, 'n': 3, 'b': 3, 'q': 9, 'k': float('inf')   
}
col_not = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
#row = 8 - given
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],  
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],  
    ['', '', '', '', '', '', '', ''],         
    ['', '', '', '', '', '', '', ''],         
    ['', '', '', '', '', '', '', ''],         
    ['', '', '', '', '', '', '', ''],           
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']   
]
def decode_input(move):
    move_start_row = 8 - int(move[1])
    move_start_col = col_not[move[0]]
    move_end_row = 8 - int(move[3])
    move_end_col = col_not[move[2]]
    return [move_start_row, move_start_col, move_end_row, move_end_col]
def pawn_move(board, move):
    move = decode_input(move)
    print('start:', board[move[0]][move[1]])
    print('end: ', board[move[2]][move[3]])


pawn_move(board, 'd2d4')
for row in board:
    fr = ''
    for i in row:
        fr += (i.center(2) + ' ') # keep the squarity of the board while printing
    print(fr)