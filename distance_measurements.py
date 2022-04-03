import numpy as np


def minkowski_distance(x, y, alpha):
    distance = 0
    for x_i in x:
        for y_i in y:
            distance += abs(x_i-y_i)**alpha
    distance**(1/alpha)
    return distance


x = (2.6, 3)
y = (2.6, 2.3)

print(minkowski_distance(x, y, 2))
