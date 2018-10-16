
#from player import Player

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[' ']*self.width for i in range(self.height)]
    
    def add_piece(self, col, piece):
        for row in range(self.height-1,-1,-1):
            if self.board[row][col-1] == ' ':
                self.board[row][col-1] = piece
                break
        else:
            raise ValueError
    
    def empty_board(self):
        self.board = [[' ']*self.width for i in range(self.height)]
    
    def check_win(self):
        for i in range(self.height):
            for c in range(self.width-4):
                if self.board[i][c] == self.board[i][c+1] == self.board[i][c+2] == self.board[i][c+3] != ' ':
                    print(True)
                    break
        for c in range(self.width):
            for r in range(self.height-3):
                if self.board[r][c] == self.board[r+1][c] == self.board[r+2][c] == self.board[r+3][c] != ' ':
                    print(True)
                    break
        for i in range(self.height-3):
            for c in range(self.width-3):
                if self.board[i][c] == self.board[i+1][c+1] == self.board[i+2][c+2] == self.board[i+3][c+3] != ' ':
                    print(True)
                    break
        for i in range(self.height-3):
            for c in range(self.width-3,self.height+1,-1):
                if self.board[i][c] == self.board[i+1][c-1] == self.board[i+2][c-2] == self.board[i+3][c-3] != ' ':
                    print(True)
                    break
        
                
    
    def is_full(self):
        pass
    
    def disp_board(self):
        colnum = ""
        print("--" * self.width)
        for row in self.board:
            for ele in row:
                print(ele,end=" ")
            print()        
        print("--" * self.width)
        for i in range(self.width):
            colnum = (colnum + str(i+1)+' ')
        print(colnum)
            



def main():
    b = Board(6,6)
    b.disp_board()
    b.add_piece(1,'v')
    b.add_piece(2,'t')
    b.add_piece(2,'v')
    b.add_piece(3,'t')
    b.add_piece(3,'t')
    b.add_piece(3,'v')
    b.add_piece(4,'t')
    b.add_piece(4,'t')
    b.add_piece(4,'t')
    b.add_piece(4,'v')
    b.disp_board()
    b.check_win()


if __name__ == "__main__":
    # test code
    main()

        
