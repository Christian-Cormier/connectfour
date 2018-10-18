class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        
        self.piece = piece
    def get_name(self):
        return input("what is your name-- ")
    def get_choice(self,board):
        choice = int(input(f'now {self.name} pick a column-- '))
        return(int(choice))

        


    
