#******************************************************************************
# tictactoe.py
#******************************************************************************
# Name: Eduardo Esteves
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

#initiate class
class TTTBoard:
    def __init__ (self):
        self._board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
    #display the board    
    def display(self):
        for line in self._board:
            for element in line:
                print(f'{element:2}', end = '')
            print()
        print()
        
    #set a value on the board    
    def set(self, row, column, xo):
        self._board[row][column] = xo
        
    #return true if the spot on the board is not empty
    def occupied(self, row, column):
        return self._board[row][column] != ' '
    
    #if a row contains the same value
    def row_full(self, row, xo):
        return self._board[row][0] == xo and self._board[row][1] == xo and self._board[row][2] == xo
    
    #if a column contains the same value
    def col_full(self, column, xo):
        return self._board[0][column] == xo and self._board[1][column] == xo and self._board[2][column] == xo
    
    #if either way diagonally has the same value
    def diag_full(self, xo):
        diag1 = self._board[0][0] == xo and self._board[1][1] == xo and self._board[2][2] == xo
        
        diag2 = self._board[0][2] == xo and self._board[1][1] == xo and self._board[2][0] == xo
        
        return diag1 or diag2
    #apply col/row/diag .full to determine if any of them is true for a value, hence a winner
    def win_for(self, xo):
        #first check diagonally
        if self.diag_full(xo):
            return True
        #loop checks for colums and rows
        for row_or_col in range(3):
            if self.row_full(row_or_col, xo) or self.col_full(row_or_col, xo):
                return True
        #otherwise False
        return False
    
    def random_move(self, xo):
        #check if there are empty spots to start with
        empty_spot = False
        for line in range(3):
            for element in range(3):
                if not self.occupied(line, element):
                    empty_spot = True
                    
        import random 
        
        added = False
        #if there are empty spots and an elemnt has not been added the lop runs
        while empty_spot and not added:
            #randomly select a spot
            row = random.randrange(0,3)
            col = random.randrange(0,3)
            if not self.occupied(row, col):
                self.set(row, col, xo)
                added = True
                
            
            



def main():
    ############################################################################
    # TEST CODE: DO NOT REMOVE IN FINAL SUBMISSION!
    ############################################################################
    myGame = TTTBoard()
    myGame.display()

    # Only run the following lines after you've written .set()
    # This should print something that looks kind of like
    # x o x
    # o x
    # x
    myGame.set(0, 0, 'x')
    myGame.set(0, 1, 'o')
    myGame.set(0, 2, 'x')
    myGame.set(1, 0, 'o')
    myGame.set(1, 1, 'x')
    myGame.set(2, 0, 'x')
    myGame.display()

    # Only run the following lines after you've written .occupied()
    # This should print out
    # True True True
    # True True False
    # True False False
    print(myGame.occupied(0,0),myGame.occupied(0,1),myGame.occupied(0,2))
    print(myGame.occupied(1,0),myGame.occupied(1,1),myGame.occupied(1,2))
    print(myGame.occupied(2,0),myGame.occupied(2,1),myGame.occupied(2,2))
    
    
    # Only run the following lines after you've written .win_for()
    # This should print out:
    # True
    # False
    print(myGame.win_for('x'))
    print(myGame.win_for('o'))

    # Only run the following lines after you've written .random_move()
    myGame.random_move('x')
    myGame.display()
    myGame.random_move('o')
    myGame.display()


    ############################################################################
    # END OF TEST CODE.
    # PLACE YOUR SIMULATION CODE BELOW.
    ############################################################################
    
    trials = 10000
    x_wins = 0
    
    for trial in range(trials):
        test_game = TTTBoard()
        
        for move in range(9):
            test_game.random_move('x')
            if test_game.win_for('x'):
                x_wins += 1
                break
            test_game.random_move('o')
            if test_game.win_for('o'):
                break
        
    print(f'Proabability x is the winner: {x_wins/trials}')
                
    
    
    

    

main()
