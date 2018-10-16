from board import Board
from player import Player

class Game:
    def __init__(self):
        self.turn = 0
        self.players = []
        self.players.append(Player('*'))
        self.players.append(Player('$'))
        self.board = Board(6,7)

    def winner(self):
        if check_win() == True:
            print("You Win!")
        if check_win() == False:
            #repeat
            pass
            
    def check_full(self):
        if is_full() == True:
            print("You Tie!")
        if is_full() == False:
            #continue as normal
            pass
    def play_game(self):
        print("Welcome To Connect 4!")
        Player.get_choice(self,self.board)
        turn = (turn + 1) % 2

if __name__ == "__main__":
    g = Game()
    g.play_game()
    
#while True:
#    board.addpiece()
    