from board import Board
from player import Player

class Game:
    def __init__(self,board):
        self.turn = 0
        self.players = []
        self.board = board

        
    def play_game(self):
        print("Welcome To Connect 4!")
        print(' ')
        print('Player 1 what is your name')
        self.players.append(Player('*'))
        print('Player 2 what is your name')
        self.players.append(Player('$'))
        while True:
            print(self.turn)
#            try:
            self.board.disp_board()
            self.choice = self.players[self.turn].get_choice(self.board)
            self.board.add_piece(self.choice,self.players[self.turn].piece)
            if self.board.check_win():
                self.board.disp_board()
                print('You Win!')
                return
            if self.board.is_full():
                self.board.disp_board()
                print('You Tie!')
                return
            self.turn = (self.turn + 1) % 2 
#            except Exception as e:
#                print(e)
                
if __name__ == "__main__":
    g = Game(Board(7,7))
    g.play_game()

    