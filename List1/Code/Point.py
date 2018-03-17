class Point:
    x = 0.0
    y = 0.0
    value = 0

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def getX(self):
        return self.x

    def getY(self):
        return self.y
