
#from player import Player

class Board:
    def __init__(self):
        self.width = int(input("How many columns are in your Connect Four board?"))
        self.height = int(input("How many rows are in your Connect Four board?"))
        self.board = [[' ']*self.width for i in range(self.height)]
    
    def place_piece(self, piece, col):
        piece = Player.players[Game.turn//2].piece
        col = Player.players[Game.turn//2].get_choice(self)
    
    def empty_board(self):
        pass
    
    def check_win():
        pass
    
    def is_full():
        pass
    
    def disp_board():
        pass



def main():
    Board()
    print(Board.board)


if __name__ == "__main__":
    # test code
    main()

        
