import chess as ch
import random
class Main:
    def __init__(self):
        self.board = ch.Board()
        self.pos_searched = 0
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
        self.pos_searched += 1
        if self.pos_searched % 10000 == 0:
            print(f"{self.pos_searched:,}")
        if depth == 0 or self.board.is_game_over():
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

    def best_move(self, depth):
        best_move = None
        best_val = -float('inf') if self.board.turn == ch.WHITE else float('inf')
        alpha = -float('inf')
        beta = float('inf')
        for move in self.board.legal_moves:
            self.board.push(move)
            board_val = self.minimax(depth - 1, alpha, beta, not self.board.turn)
            self.board.pop()
            if self.board.turn: 
                if board_val > best_val:
                    best_val = board_val
                    best_move = move
            else:  
                if board_val < best_val:
                    best_val = board_val
                    best_move = move
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
                    self.pos_searched = 0
                    self.hooman()
                else:
                    self.board.push(self.best_move(depth = 5))
            res = self.board.result()
            print(res)
        except KeyboardInterrupt:
            print("exit")

game = Main()
game.start_game()
