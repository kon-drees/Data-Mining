import numpy as np


# alpha = 2 for euclid, = 1 for manhattan, alpha -> infinity for tschebyschew distance
def minkowski_distance(x, y, alpha):
    array1, array2 = np.array(x), np.array(y)
    distance = sum(abs(array1-array2)**alpha)**(1/alpha)
    return distance


def tschebyschew_distance(x,y):
    array1, array2 = np.array(x), np.array(y)
    distance = abs(array1-array2)
    return max(distance)


# cosinus similarity
def cos_sim(x, y):
    array1, array2 = np.array(x), np.array(y)
    similarity = (np.dot(array1, array2))/(np.sqrt(sum(array1**2))*np.sqrt(sum(array2**2)))
    return similarity


x1 = (2.6, 3)
x2 = (2.3, 2.9)
x3 = (2.3, 1.6)
x4 = (2.7, 2.8)
x5 = (1.9, 2.2)
x_list = (x1, x2, x3, x4, x5)
y = (2.6, 2.3)

for x in x_list:
    print(f"Manhattan: {minkowski_distance(x, y, 1)}")
    print(f"Euclid: {minkowski_distance(x, y, 2)}")
    print(f"Tschebyschew: {tschebyschew_distance(x, y)}")
    print(f"Similarity : {cos_sim(x, y)}")
    print("---------------------------------")

#distances 
x_norm = []
for element in x_list:
    x_norm.append(tuple(element/minkowski_distance(element, (0,0), 2)))
print(x_norm)

y_norm = tuple(y/minkowski_distance(y, (0,0), 2))
for x in x_norm:
    print(f"Euclid: {minkowski_distance(x, y_norm, 2)}")
    print("---------------------------------")

