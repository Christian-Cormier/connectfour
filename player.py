class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        #self.choice = self.get_choice(Board)
        self.piece = piece
    def get_name(self):
        return input("what is your name-- ")
    def get_choice(self,board):
        choice = int(input(f'now {self.name} pick a column-- '))
#        if choice != int:
#            print('your choice has to be an integer')
#            get_choice()
        if choice < 0:
            print('your choice has to be greater than 0')
            get_choice()
        if choice > board.width:     
            print('your choice is greater than the width of the board')
            get_choice()
        

def main():
    p1 = Player('x')
    print(p1.get_choice(6))
    
if __name__ == "__main__":
    main()