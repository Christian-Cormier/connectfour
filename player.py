class Player:
    def __init__(self,piece):
        self.name = self.get.name()
        self.piece = piece
    def get_name(self):
        name = input("what is your name-- ")
    def get_choice(self, Board):
        choice = input(int("where do you want to place your piece by column-- "))
        if choice != int:
            print('your choice has to be an integer')
        if choice < 0:
            print('your choice has to be greater than 0')
            get_choice()
        if choice > width:
            print('your choice is greater than the width of the board')
        else: 
            return(choice)

