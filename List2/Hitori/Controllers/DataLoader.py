import xlrd
import numpy


class DataLoader:
    @staticmethod
    def loadData(file_path):
        data = []
        workbook = xlrd.open_workbook(file_path)
        sheets = workbook.sheet_names()
        for sheet in sheets:
            current_sheet = workbook.sheet_by_name(sheet)
            rows = current_sheet.nrows
            columns = current_sheet.ncols
            data = numpy.zeros((rows, columns))
            for row in range(0, rows):
                for column in range(0, columns):
                    data[row, column] = int(current_sheet.cell(rowx=row, colx=column).value)
        return numpy.array(data)
