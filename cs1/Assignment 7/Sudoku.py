'''
This program allows the user to interactively play the game of Sudoku.
'''

import sys

class SudokuError(Exception):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass

class Sudoku:
    '''Interactively play the game of Sudoku.'''

    def __init__(self):
        self.board = []
        self.moves = []
        
        for i in range(9):
            self.board.append([])
            for j in range(9):
                self.board[i].append(0)        

    def load(self, filename):
        file = open(filename, 'r')
        i = 0
        for i in range(9):
            line = file.readline()
            line = line[:9]
            for j in range(9):
                self.board[i][j] = int(line[j]) 
        self.moves = []
        file.close()
            
    def save(self, filename):
        file = open(filename, 'w')
        for i in range(9):
            for j in range(9):
                file.write(str(self.board[i][j]))
            file.write('\n')
        file.close()

    def show(self):
        '''Pretty-print the current board representation.'''
        print()
        print('   1 2 3 4 5 6 7 8 9 ')
        for i in range(9):
            if i % 3 == 0:
                print('  +-----+-----+-----+')
            sys.stdout.write('%d |' % (i + 1))
            for j in range(9):
                if self.board[i][j] == 0:
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('%d' % self.board[i][j])
                if j % 3 != 2 :
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('|')
            print() 
        print('  +-----+-----+-----+')
        print()

    def move(self, row, col, val):
        row = row - 1
        col = col - 1
        if 0 > row or row > 8 and type(row) is not int:
            raise SudokuMoveError('The row coordinate must be an integer greater than 0 and smaller than 10.')
        elif 0 > col or col > 8 and type(col) is not int:
            raise SudokuMoveError('The column coordinate must be an integer greater than 0 and smaller than 10.')
        elif 0 > val or val > 8 and type(val) is not int:
            raise SudokuMoveError('The value must be an integer greater than 0 and smaller than 10.')
        elif self.board[row][col] != 0:
            raise SudokuMoveError('Invalid move: occupied space, please try again.')
        for i in range(9):
            if self.board[i][col] == val:
                raise SudokuMoveError('Invalid move: column conflict, please try again.')
            elif self.board[row][i] == val:
                raise SudokuMoveError('Invalid move: row conflict, please try again.')
            
        if row <= 3:
            row_range = 0, 3
        elif row >= 4 and row <= 6:
            row_range = 3, 6
        elif row >= 7 and  row <= 9:
            row_range = 6, 9
        
        if col <= 3:
            col_range = 0, 3
        elif col >= 4 and col <= 6:
            col_range = 3, 6
        elif col >= 7 and col <= 9:
            col_range = 6, 9
        
        for i in range(row_range[0], row_range[1]):
            for j in range(col_range[0], col_range[1]):
                if self.board[i][j] == val:
                    raise SudokuMoveError('Invalid move: box conflict, please try again.')
        
        self.board[row][col] = val
        self.moves.append([row, col, val])
        
    def undo(self):
        elements = self.moves.pop()
        self.board[elements[0]][elements[1]] = 0

    def solve(self):
        command = input('Introduce the command: ')
        while True:
            try:
                if command == 'q':
                    return
                elif len(command) == 3:
                    self.move(int(command[0]), int(command[1]), int(command[2]))
                    self.show()
                elif command == 'u':
                    self.undo()
                    self.show()
                elif command[0] == 's':
                    command = command.split()
                    self.save(command[1])
                else:
                    raise SudokuCommandError(command)
                
            except SudokuCommandError:
                print('%s is an invalid command please try again.'%command)
            except SudokuMoveError as e:
                print(e)
                
            command = input('Introduce the command: ')            
                

if __name__ == '__main__':
    s = Sudoku()

    while True:
        filename = input('Enter the sudoku filename: ')
        try:
            s.load(filename)
            break
        except IOError as e:
            print(e)

    s.show()
    s.solve()

