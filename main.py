import chess as ch
import time

class Main:
    def __init__(self):
        self.board = ch.Board()
        self.pos_searched = 0
        self.to_search = 10
        self.transposition_table = {}
        self.board.set_fen('rnbqkb1r/pppppppp/4n3/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1')
    def evaluate(self):
        vals = {
            ch.ROOK: 5.63,
            ch.PAWN: 1,
            ch.BISHOP: 3.33,
            ch.KNIGHT: 3.2,  
            ch.QUEEN: 9.5,
        }
        eval = 0
        if self.board.is_checkmate():
            return float('-inf') if self.board.turn == ch.BLACK else float('inf')
        elif self.board.is_stalemate() or self.board.is_insufficient_material():
            return 0

        for piece_type in vals:
            eval += len(self.board.pieces(piece_type, ch.WHITE)) * vals[piece_type] 
            eval -= len(self.board.pieces(piece_type, ch.BLACK)) * vals[piece_type] 
        return eval

    def minimax(self, depth, alpha, beta, is_maximizing):
        board_hash = self.board._transposition_key()

        if board_hash in self.transposition_table and self.transposition_table[board_hash][0] >= depth:
            return self.transposition_table[board_hash][1]
        
        self.pos_searched += 1
        if self.pos_searched % 10000 == 0:
            print(f"{self.pos_searched:,}")
        
        if self.board.is_checkmate():
            return float('-inf') if self.board.turn == ch.BLACK else float('inf')

        if self.board.is_game_over():
            return 0  
        
        if depth == 0:
            return self.evaluate()

        if is_maximizing:
            max_eval = -float('inf')
            for move in self.board.legal_moves:
                self.board.push(move)
                eval = self.minimax(depth - 1, alpha, beta, False)
                self.board.pop()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.board.legal_moves:
                self.board.push(move)
                eval = self.minimax(depth - 1, alpha, beta, True)
                self.board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break 
            return min_eval

    def best_move(self):
        start_time = time.time()
        best_move = None
        best_val = float('inf')  
        alpha = -float('inf')
        beta = float('inf')
        
        depth = 1
        mate_threshold = 10000 
        while True:
            if time.time() >= (start_time + self.to_search):
                break
            
            print(f'depth: {depth}')
            
            found_mate = False
            
            for move in self.board.legal_moves:
                if time.time() >= (start_time + self.to_search):
                    break
                self.board.push(move)
            
                move_val = self.minimax(depth - 1, alpha, beta, is_maximizing=self.board.turn == ch.WHITE)
                self.board.pop()
                
                if move_val < best_val:
                    best_val = move_val
                    best_move = move

                if abs(move_val) > mate_threshold - depth:
                    found_mate = True
                    print(f'Mate detected at depth {depth} with move {move}')
                    break  

            if found_mate:
                print(f'Stopping search due to mate found at depth {depth}')
                break
            
            depth += 1
            

            if time.time() >= (start_time + self.to_search):
                break

        end_time = time.time()
        print(f'Time taken: {end_time - start_time:.4f}')
        print(f'Best move: {best_move}')
        return best_move

    def hooman(self):
        print(self.board)
        try:
            play = input("whites turn: ")
            self.board.push_san(play)
        except ValueError:
            print('nope, thats not allowed')
            self.hooman()

    def hooman2(self):
        print(self.board)
        try:
            play = input("blacks turn: ")
            self.board.push_san(play)
        except ValueError:
            print('nope, thats not allowed')
            self.hooman2()

    def start_game(self):
        try:
            while not self.board.is_game_over():
                print(self.evaluate())
                print(self.board.legal_moves)
                if self.board.turn:
                    self.hooman()
                else:
                    self.pos_searched = 0
                    self.board.push(self.best_move())
            res = self.board.result()
            print(res)
        except KeyboardInterrupt:
            print("exit")

game = Main()
game.start_game()
