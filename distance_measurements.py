import numpy as np


# alpha = 2 for euclid, = 1 for manhattan, alpha -> infinity for tschebyschew distance
def minkowski_distance(x, y, alpha):
    array1, array2 = np.array(x), np.array(y)
    distance = sum(abs(array1-array2)**alpha)**(1/alpha)
    return distance


# cosinus similarity
def cos_sim(x, y):
    array1, array2 = np.array(x), np.array(y)
    similarity = (np.dot(array1, array2))/(np.sqrt(sum(array1**2))*np.sqrt(sum(array2**2)))
    return similarity


x = (2.6, 3)
y = (2.6, 2.3)

print(minkowski_distance(x, y, 2))
print(cos_sim(x, y))
