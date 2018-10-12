
#from player import Player

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[' ']*self.width for i in range(self.height)]
    
    def add_piece(self, col, piece):
        for row in range(len(self.board)):
            for column in range((row)):
                if col == column and self.board[row][col] != ' ':
                    self.board[row-1][col] = piece
    
    def empty_board(self):
        self.board = [[' ']*self.width for i in range(self.height)]
    
    def check_win(self):
        pass
    
    def is_full(self):
        pass
    
    def disp_board(self):
        colnum = ""
        print("--" * self.width)
        for row in self.board:
            for ele in row:
                print(ele,end=' ')
        print("--" * self.width)
        for i in range(self.width):
            colnum = (colnum + str(i+1)+' ')
        print(colnum)
            



def main():
    b = Board(6,7)
    b.disp_board()


if __name__ == "__main__":
    # test code
    main()

        
