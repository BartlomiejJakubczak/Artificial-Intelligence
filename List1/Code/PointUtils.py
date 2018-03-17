import random
import numpy as np
import matplotlib.pyplot as plt
from List1.Point import Point

# https://stackoverflow.com/questions/
# 44356063/how-to-generate-a-set-of-random-points-within-a-given-x-y-coordinates-in-an-x
# line 14


class PointUtils:

    def generatePoints(self, number_of_points, center, radius, value):
        x, y = center
        points = []
        for i in range(number_of_points):
            theta = 2 * np.math.pi * random.random()
            s = radius * random.random()
            points.append(Point((x + s * np.math.cos(theta)), y + s * np.math.sin(theta), value))
        return np.array(points)

    def coordinatesOfPoints(self, array_of_points):
        x = []
        y = []
        for point in array_of_points:
            x.append(point.x)
            y.append(point.y)
        return np.array(x), np.array(y)
