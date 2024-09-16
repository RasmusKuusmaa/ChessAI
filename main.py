import chess as ch

class Main:
    def __init__(self):
        self.board = ch.Board()
    
    def hooman(self):
        print(self.board)
        try:
            play = input("whites turn: ")
            self.board.push_san(play)
        except:
            print('nope, thats not allowed')
            self.hooman()

    def hooman2(self):
        print(self.board)
        try:
            play = input("blacks turn: ")
            self.board.push_san(play)
        except:
            print('nope, thats not allowed')
            self.hooman2()

    def start_game(self):
        while not self.board.is_game_over():
            print(self.board.legal_moves)
            # self.board.turn returns true if it is whites turn
            if self.board.turn:
                self.hooman()
            else:
                self.hooman2()

        res = self.board.result()
        print(res)
game = Main()
game.start_game()
