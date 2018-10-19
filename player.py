class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        self.piece = piece
    def get_name(self):
        '''
        gets the users name using user input
        '''
        return input("what is your name-- ")
    def get_choice(self,board):
        '''
        gets the column number from the player by user input
        '''
        choice = int(input(f'now {self.name} pick a column-- '))
        return(int(choice))

        


    
