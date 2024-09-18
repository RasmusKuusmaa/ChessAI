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
                    self.hooman2()
            res = self.board.result()
            print(res)
        except KeyboardInterrupt:
            print("exit")
game = Main()
game.start_game()
