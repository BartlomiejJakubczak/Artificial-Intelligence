class Square:
    value = 0
    row_position, column_position = 0, 0
    correct = False
    shaded = False

    def __init__(self, value, row, column):
        self.value = value
        self.row_position = row
        self.column_position = column

    def setCorrect(self, boolean_value):
        if boolean_value is True:
            self.shaded = False
        self.correct = boolean_value

    def setShaded(self, board, boolean_value):
        if boolean_value is True:
            if self.row_position == 0:  # if you are at the top
                if self.column_position - 1 < 0:  # to the left
                    self.shaded = True
                    board.squares[self.row_position, self.column_position + 1].setCorrect(True)
                    board.squares[self.row_position + 1, self.column_position].setCorrect(True)
                else:
                    if self.column_position + 1 > board.squares.shape[1] - 1:  # to the right
                        self.shaded = True
                        board.squares[self.row_position, self.column_position - 1].setCorrect(True)
                        board.squares[self.row_position + 1, self.column_position].setCorrect(True)
                    else:  # in between
                        self.shaded = True
                        board.squares[self.row_position, self.column_position - 1].setCorrect(True)
                        board.squares[self.row_position, self.column_position + 1].setCorrect(True)
                        board.squares[self.row_position + 1, self.column_position].setCorrect(True)
            else:
                if self.row_position in range(1, board.squares.shape[0] - 1):  # from row 1 to 6
                    if self.column_position - 1 < 0:  # to the left
                        self.shaded = True
                        board.squares[self.row_position + 1, self.column_position].setCorrect(True)
                        board.squares[self.row_position - 1, self.column_position].setCorrect(True)
                        board.squares[self.row_position, self.column_position + 1].setCorrect(True)
                    else:
                        if self.column_position + 1 > board.squares.shape[1] - 1:  # to the right
                            board.squares[self.row_position + 1, self.column_position].setCorrect(True)
                            board.squares[self.row_position - 1, self.column_position].setCorrect(True)
                            board.squares[self.row_position, self.column_position - 1].setCorrect(True)
                        else:  # in between
                            board.squares[self.row_position + 1, self.column_position].setCorrect(True)
                            board.squares[self.row_position - 1, self.column_position].setCorrect(True)
                            board.squares[self.row_position, self.column_position - 1].setCorrect(True)
                            board.squares[self.row_position, self.column_position + 1].setCorrect(True)
                else:
                    if self.row_position == board.squares.shape[0] - 1:  # if you are at the bottom
                        if self.column_position - 1 < 0:  # to the left
                            self.shaded = True
                            board.squares[self.row_position, self.column_position + 1].setCorrect(True)
                            board.squares[self.row_position - 1, self.column_position].setCorrect(True)
                        else:
                            if self.column_position + 1 > board.squares.shape[1] - 1:  # to the right
                                self.shaded = True
                                board.squares[self.row_position, self.column_position - 1].setCorrect(True)
                                board.squares[self.row_position - 1, self.column_position].setCorrect(True)
                            else:
                                self.shaded = True  # in between
                                board.squares[self.row_position, self.column_position - 1].setCorrect(True)
                                board.squares[self.row_position, self.column_position + 1].setCorrect(True)
                                board.squares[self.row_position - 1, self.column_position].setCorrect(True)
        else:  # in case of unshading
            if self.row_position == 0:  # if you are at the top
                if self.column_position - 1 < 0:  # to the left
                    self.shaded = False
                    board.squares[self.row_position, self.column_position + 1].setCorrect(False)
                    board.squares[self.row_position + 1, self.column_position].setCorrect(False)
                else:
                    if self.column_position + 1 > board.squares.shape[1] - 1:  # to the right
                        self.shaded = False
                        board.squares[self.row_position, self.column_position - 1].setCorrect(False)
                        board.squares[self.row_position + 1, self.column_position].setCorrect(False)
                    else:  # in between
                        self.shaded = False
                        board.squares[self.row_position, self.column_position - 1].setCorrect(False)
                        board.squares[self.row_position, self.column_position + 1].setCorrect(False)
                        board.squares[self.row_position + 1, self.column_position].setCorrect(False)
            else:
                if self.row_position in range(1, board.squares.shape[0] - 1):  # from row 1 to 6
                    if self.column_position - 1 < 0:  # to the left
                        self.shaded = False
                        board.squares[self.row_position + 1, self.column_position].setCorrect(False)
                        board.squares[self.row_position - 1, self.column_position].setCorrect(False)
                        board.squares[self.row_position, self.column_position + 1].setCorrect(False)
                    else:
                        if self.column_position + 1 > board.squares.shape[1] - 1:  # to the right
                            board.squares[self.row_position + 1, self.column_position].setCorrect(False)
                            board.squares[self.row_position - 1, self.column_position].setCorrect(False)
                            board.squares[self.row_position, self.column_position - 1].setCorrect(False)
                        else:  # in between
                            board.squares[self.row_position + 1, self.column_position].setCorrect(False)
                            board.squares[self.row_position - 1, self.column_position].setCorrect(False)
                            board.squares[self.row_position, self.column_position - 1].setCorrect(False)
                            board.squares[self.row_position, self.column_position + 1].setCorrect(False)
                else:
                    if self.row_position == board.squares.shape[0] - 1:  # if you are at the bottom
                        if self.column_position - 1 < 0:  # to the left
                            self.shaded = False
                            board.squares[self.row_position, self.column_position + 1].setCorrect(False)
                            board.squares[self.row_position - 1, self.column_position].setCorrect(False)
                        else:
                            if self.column_position + 1 > board.squares.shape[1] - 1:  # to the right
                                self.shaded = False
                                board.squares[self.row_position, self.column_position - 1].setCorrect(False)
                                board.squares[self.row_position - 1, self.column_position].setCorrect(False)
                            else:
                                self.shaded = False  # in between
                                board.squares[self.row_position, self.column_position - 1].setCorrect(False)
                                board.squares[self.row_position, self.column_position + 1].setCorrect(False)
                                board.squares[self.row_position - 1, self.column_position].setCorrect(False)

    def __str__(self):
        if self.correct is False and self.shaded is False:
            correct = "-"
            shaded = "-"
            return str(int(self.value)) + correct + shaded
        else:
            correct = "T" if self.correct is True else "F"
            shaded = "T" if self.shaded is True else "F"
            return str(int(self.value)) + correct + shaded

    def __repr__(self):
        return str(self)
