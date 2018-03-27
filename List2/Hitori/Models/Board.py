import numpy

from List2.Hitori.Models.Square import Square


class Board:
    squares = []

    def __init__(self, shape):
        self.squares = numpy.zeros((shape, shape))

    def prepareBoard(self, data):
        # Create for each place of squares Square object with given value
        self.squares = [Square(data[i][j], i, j) for i in range(data.shape[0]) for j in range(data.shape[1])]
        # Recreate dimensions as a numpy array
        self.squares = numpy.asarray(self.squares).reshape((data.shape[0], data.shape[1]))

    def __str__(self):
        string = [self.squares[i, j] for i in range(self.squares.shape[0]) for j in range(self.squares.shape[1])]
        string = numpy.asarray(string).reshape((self.squares.shape[0], self.squares.shape[1]))
        return str(string)
