import numpy

from List2.Hitori.Controllers.Algorithm import Algorithm
from List2.Hitori.Controllers.DataLoader import DataLoader
from List2.Hitori.Models.Board import Board
from List2.Hitori.Models.Square import Square

if __name__ == '__main__':
    hitori = Board(8)

    hitori.prepareBoard(DataLoader.loadData("E:\Studia\Semestr VI\Artificial Intelligence\Puzzles\Puzzle_8x8.xlsx"))
    print(hitori)
    print()
    Algorithm.initialPreparation(hitori)
    print(hitori)
