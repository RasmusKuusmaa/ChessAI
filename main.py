import chess as ch
import random
import time

class Main:
    def __init__(self):
        self.board = ch.Board()
        self.pos_searched = 0
        self.to_search = 5000
        self.transposition_table = {}
        #self.board.set_fen('')

    def evaluate(self):
        vals = {
            ch.ROOK: 5,
            ch.PAWN: 1,
            ch.BISHOP: 3,
            ch.KNIGHT: 3,
            ch.QUEEN: 9,
        }
        eval = 0
        for type in vals:
            eval += len(self.board.pieces(type, ch.WHITE)) * vals[type] + random.randint(0, 100) * 0.000001
            eval -= len(self.board.pieces(type, ch.BLACK)) * vals[type] + random.randint(0, 100) * 0.000001
        return eval

    def minimax(self, depth, alpha, beta, is_maximizing):
        
        board_hash = hash(self.board.fen())
        if board_hash in self.transposition_table and self.transposition_table[board_hash][0] >= depth:
            return self.transposition_table[board_hash][1]
        self.pos_searched += 1
        if self.pos_searched % 10000 == 0:
            print(f"{self.pos_searched:,}")
                
        if depth == 0 or self.board.is_game_over():
            eval = self.evaluate()
            self.transposition_table[board_hash] = (depth, eval)
            return eval
   
   
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
            self.transposition_table[board_hash] = (depth, max_eval)
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
            self.transposition_table[board_hash] = (depth, min_eval)
            return min_eval

    def best_move(self):
        start_time = time.time()
        best_move = None
        best_val = -float('inf') if self.board.turn == ch.WHITE else float('inf')
        alpha = -float('inf')
        beta = float('inf')
        
        depth = 1
        while True:
            if time.time() >= (start_time + self.to_search):
                break
            
            print('depth: ', depth)            
            for move in self.board.legal_moves:
                if time.time() >= (start_time + self.to_search):
                    break
                self.board.push(move)
                move_val = self.minimax(depth - 1, alpha, beta, not self.board.turn)
                self.board.pop()
                
                if self.board.turn:
                    if move_val > best_val:
                        best_val = move_val
                        best_move = move
                else:
                    if move_val < best_val:
                        best_val = move_val
                        best_move = move
            depth += 1
            if time.time() >= (start_time + self.to_search):
                break

        end_time = time.time()
        print(f'Time taken: {end_time - start_time:.4f}')
        print(best_move)
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