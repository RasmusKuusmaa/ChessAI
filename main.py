import chess as ch

class Main:
    def __init__(self):
        self.board = ch.Board()

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
            eval += len(self.board.pieces(type, ch.WHITE)) * vals[type]
            eval -= len(self.board.pieces(type, ch.BLACK)) * vals[type]
        return eval

    def minimax(self, depth, is_maximizing):
        if depth == 0 or self.board.is_game_over():
            return self.evaluate()
        if is_maximizing:
            max_eval = -float('inf')
            for move in self.board.legal_moves:
                self.board.push(move)
                eval = self.minimax(depth - 1, False)
                self.board.pop()
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.board.legal_moves:
                self.board.push(move)
                eval = self.minimax(depth - 1, True)
                self.board.pop()
                min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self, depth):
        best_move = None
        best_val = -float('inf') if self.board.turn == ch.WHITE else float('inf')
        for move in self.board.legal_moves:
            self.board.push(move)
            board_val = self.minimax(depth - 1, not self.board.turn)
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
                    self.hooman()
                else:
                    self.board.push(self.best_move(depth = 2))
            res = self.board.result()
            print(res)
        except KeyboardInterrupt:
            print("exit")

game = Main()
game.start_game()
