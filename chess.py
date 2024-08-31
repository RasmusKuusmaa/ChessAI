pieces = {
    'P': 1, 'R': 5, 'N': 3, 'B': 3, 'Q': 9, 'K': float('inf'),  
    'p': 1, 'r': 5, 'n': 3, 'b': 3, 'q': 9, 'k': float('inf')   
}
col_not = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
#row = 8 - given
board = [
    ['Br', 'Bn', 'Bb', 'Bq', 'Bk', 'Bb', 'Bn', 'Br'],  
    ['Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp', 'Bp'],  
    ['', '', '', '', '', '', '', ''],         
    ['', '', '', '', '', '', '', ''],         
    ['', '', '', '', '', '', '', ''],         
    ['', '', '', '', '', '', '', ''],           
    ['Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp', 'Wp'],  
    ['Wr', 'Wn', 'Wb', 'Wq', 'Wk', 'Wb', 'Wn', 'Wr']   
]
def decode_input(move):
    move_start_row = 8 - int(move[1])
    move_start_col = col_not[move[0]]
    move_end_row = 8 - int(move[3])
    move_end_col = col_not[move[2]]
    return [move_start_row, move_start_col, move_end_row, move_end_col]
move_count = 0
def pawn_move(board, move):
    move = decode_input(move)
    piece_to_move = board[move[0]][move[1]]
    
    if piece_to_move[1] != 'p':
        print(1)
        return False
    

    distance = move[2] - move[0]
    if move[1] != move[3]:
        #capture
        if abs(move[1] - move[3]) == 1:
            if abs(move[0] - move[2]) != 1:
                print(2)
                return False
            if abs(distance) != 1:
                print(3)
                return False
    
    elif board[move[2]][move[3]] != '':
        print(9)
        return False
    if abs(distance) <= 2:
       
        if move_count > 2:
    
            if abs(distance) != 1:
                print(5)
                return False
        if piece_to_move[0] == 'W':
            if move[0] < move[1]:
                print(6)
                return False
        elif piece_to_move[0] == 'B':
            if move[0] > move[1]:
                print(7)
                return False 
    
    else:
        print(8)
        return False
   

    board[move[0]][move[1]] = ''
    board[move[2]][move[3]] = piece_to_move
    


pawn_move(board, 'd2d4')
pawn_move(board, 'e7e5')
pawn_move(board, 'd4e5')
for index, row in enumerate(board):
    fr = f'{8 - index } '
    for i in row:
        fr += (i.center(2) + ' ') # keep the squarity of the board while printing
    print(fr)
print('  a  b  c  d  e  f  g  h  ')