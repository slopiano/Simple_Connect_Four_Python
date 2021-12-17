'''
Created on 5/9/21
@author:   Sebastian LoPiano
'''

import sys

class Board(object):

    def __init__(self, width=7, height=6):
        '''Takes the width and the heigh and creates the empty list for Connect'''
        self.width = width
        self.height = height
        self.Connect = []

    def createBoard(self, width, height):
        '''Creates the list for the connect 4 values'''
        for column in range(0,height):
            self.Connect += [self.createOneRow(width)]

    def createOneRow(self, width):
        '''Creates a row'''
        self.column = []
        for row in range(0,width):
            self.column += [' ']
        return self.column
    

    def __str__(self):
        '''Prints the board so the players can see what is going on'''
        for row in self.Connect:
            for column in row:
                if column == ' ':
                    sys.stdout.write('| ')
                else:
                    sys.stdout.write('|')
                    sys.stdout.write(str(column))
            sys.stdout.write('|')
            sys.stdout.write('\n')
        for x in range(0,15):
            sys.stdout.write('-')
        sys.stdout.write('\n')
        sys.stdout.write(' ')
        for x in range(0,self.width):
            sys.stdout.write(str(x))
            sys.stdout.write(' ')
            
    def allowsMove(self, col):
        '''Checks to see if the move is allowable'''
        if col>6 or col<0:
            return False
        if self.Connect[0][col] == ' ':
            return True
        else: return False
        
    def addMove(self, col, ox):
        '''Adds the X or O in the column specified'''
        for x in range(self.height-1,-1,-1):
            if self.Connect[x][col] == ' ':
                self.Connect[x][col] = ox
                return          

            
    '''def height(self):
        final = 0
        for x in range(self.height,0,-1):
            while self.Connect[x][y] != ' ' and y<6:
                y+=1
            if y>final and y!=6:
                final = y
                loc = x
        if final == 0:
            return 0
        else: return loc'''

    '''def addMove(self, col, ox):
        for x in range(self.height-1,-1,-1):
            if self.Connect[x][col] == ' ':
                self.Connect[x][col] = ox
                return'''

    
    def winsFor(self, ox):
        '''Checks if the player has won'''
        #Checks vertically 
        for x in range(0,self.width):
            for y in range(0,self.height-3):
                if self.Connect[y][x] == ox and self.Connect[y+1][x] == ox and self.Connect[y+2][x] == ox and self.Connect[y+3][x] == ox:
                    return True
                
        #Checks horizontally
        for x in range(0,self.height):
            for y in range(0,self.width-3):
                if self.Connect[x][y] == ox and self.Connect[x][y+1] == ox and self.Connect[x][y+2] == ox and self.Connect[x][y+3] == ox:
                    return True
                
        #Checks Diagonally
        for x in range(0, self.height-3):
            for y in range(0, self.width-3):
                if self.Connect[x][y] == ox and self.Connect[x+1][y+1] == ox and self.Connect[x+2][y+2] == ox and self.Connect[x+3][y+3] == ox:
                    return True
                
        for x in range(self.height-1, 3, -1):
            for y in range(0, self.width-3):
                if self.Connect[x][y] == ox and self.Connect[x-1][y+1] == ox and self.Connect[x-2][y+2] == ox and self.Connect[x-3][y+3] == ox:
                    return True

    def setBoard(self, moveString):
        """ takes in a string of columns and placesalternating checkers
in those columns,starting with 'X'For example, call b.setBoard('012345')to
see 'X's and 'O's alternate on thebottom row, or b.setBoard('000000') to see
them alternate in the left column.moveString must be a string of integers"""
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col,nextCh)
            if nextCh == 'X': nextCh='O'
            else: nextCh = 'X'
            
            
        
            
            
    def hostGame(self):
        '''Creates the board and starts the game, also has the order for the game to run'''
        self.createBoard(self.width,self.height)
        winner = False
        sys.stdout.write('Welcome to Connect Four')
        sys.stdout.write('\n')
        while not winner:
            self.__str__()
            sys.stdout.write('\n')
            sys.stdout.write('X\'s choice ')
            col = int(input())
            while self.allowsMove(col) != True:
                sys.stdout.write('This column is full, or this col doesnt exist')
                sys.stdout.write('\n')
                sys.stdout.write('X\'s choice ')
                col = int(input())
            self.addMove(col, 'X')
            if self.winsFor('X') == True:
                sys.stdout.write("X Wins")
                sys.stdout.write('\n')
                self.__str__()
                winner = True
            else:
                self.__str__()
                sys.stdout.write('\n')
                sys.stdout.write('O\'s choice ')
                col = int(input())
                while self.allowsMove(col) != True:
                    sys.stdout.write('This column is full, or this col doesnt exist')
                    sys.stdout.write('\n')
                    sys.stdout.write('X\'s choice ')
                    col = int(input())
                self.addMove(col, 'O')
                if self.winsFor('O') == True:
                    sys.stdout.write('O wins')
                    sys.stdout.write('\n')
                    self.__str__()
                    winner = True
        
