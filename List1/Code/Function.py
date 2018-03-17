import random


class Function:
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    evaluation_score = 0

    def __init__(self, range_start, range_end):
        self.a = random.uniform(range_start, range_end)
        self.b = random.uniform(range_start, range_end)
        self.c = random.uniform(range_start, range_end)
        self.d = random.uniform(range_start, range_end)
        self.e = random.uniform(range_start, range_end)
        self.f = random.uniform(range_start, range_end)

    def getA(self):
        return self.a

    def setA(self, a):
        self.a = a

    def getB(self):
        return self.b

    def setB(self, b):
        self.b = b

    def getC(self):
        return self.c

    def setC(self, c):
        self.c = c

    def getD(self):
        return self.d

    def setD(self, d):
        self.d = d

    def getE(self):
        return self.e

    def setE(self, e):
        self.e = e

    def getF(self):
        return self.f

    def setF(self, f):
        self.f = f

    def getEvaluationScore(self):
        return self.evaluation_score

    def setEvaluationScore(self, evaluation_score):
        self.evaluation_score = evaluation_score

    def setGene(self, number, passed_gene):
        if number == 1:
            self.a = passed_gene
        if number == 2:
            self.b = passed_gene
        if number == 3:
            self.c = passed_gene
        if number == 4:
            self.d = passed_gene
        if number == 5:
            self.e = passed_gene
        if number == 6:
            self.f = passed_gene

    def getGene(self, number):
        return{
            1: self.getA(),
            2: self.getB(),
            3: self.getC(),
            4: self.getD(),
            5: self.getE(),
            6: self.getF()
        }[number]

    def calculateValue(self, x):
        return self.getA() * pow(x, 5) + self.getB() * pow(x, 4) + \
               self.getC() * pow(x, 3) + self.getD() * pow(x, 2) + self.getE() * x + self.getF()

    def calculateFunction(self, x_array):
        y_array = []
        for x in x_array:
            value = self.getA() * pow(x, 5) + self.getB() * pow(x, 4) + \
               self.getC() * pow(x, 3) + self.getD() * pow(x, 2) + self.getE() * x + self.getF()
            y_array.append(value)
        return y_array
