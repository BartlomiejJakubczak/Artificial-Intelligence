class Algorithm:
    @staticmethod
    def initialPreparation(board):
        rows = board.squares.shape[0]
        columns = board.squares.shape[1]
        # check for correct squares in rows
        for j in range(rows):
            for i in range(1, columns - 1):
                if board.squares[j, i - 1].value == board.squares[j, i + 1].value:
                    board.squares[j, i].setCorrect(True)
        # check for correct squares in columns
        for i in range(columns):
            for j in range(1, rows - 1):
                if board.squares[j - 1, i].value == board.squares[j + 1, i].value:
                    board.squares[j, i].setCorrect(True)
        # check corners
        # upper left
        if board.squares[0, 0].value == board.squares[0, 1].value == board.squares[1, 0].value:
            board.squares[0, 0].setShaded(board, True)
        # upper right
        if board.squares[0, columns - 1].value == board.squares[0, columns - 2].value == board.squares[1, columns - 1].value:
            board.squares[0, columns - 1].setShaded(board, True)
        # lower left
        if board.squares[rows - 1, 0].value == board.squares[rows - 1, 1].value == board.squares[rows - 2, 0].value:
            board.squares[rows - 1, 0].setShaded(board, True)
        # lower right
        if board.squares[rows - 1, columns - 1].value == board.squares[rows - 1, columns - 2].value == board.squares[rows - 2, columns - 1].value:
            board.squares[rows - 1, columns - 1].setShaded(board, True)
