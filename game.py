from board import Board
from player import Player

class Game:
    def __init__(self,board):
        self.turn = 0
        self.players = []
        self.board = board

    def winner(self):
        if check_win():
            print("You Win!")
        
            
            
    def check_full(self):
        if is_full():
            print("You Tie!")
        
    def play_game(self):
        print("Welcome To Connect 4!")
        print(' ')
        print('Player 1 what is your name')
        self.players.append(Player('*'))
        print('Player 2 what is your name')
        self.players.append(Player('$'))
        while True:
            try:
                self.board.disp_board()
                self.choice = Player.get_choice(self,self.board)
                self.board.add_piece(self.choice,self.players[self.turn].piece)
                if self.board.detect_win():
                    return
                if self.board.is_full():
                    return
            except Exception as e:
                pass
if __name__ == "__main__":
    g = Game(Board(7,7))
    g.play_game()
    
#while True:
#    board.addpiece()
    