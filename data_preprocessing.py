import numpy as np


def arithmetic_mean(x,y):
    return (x+y)/2

def smooth_mean(x,y):
    return x - arithmetic_mean(x,y)

#iterative solution for a wavelet_transformations
def discrete_wavelet_transformation(data, threshold):
    step_data = list(data)
    if len(step_data) % 2 != 0:
        step_data.append(0)
    length = len(step_data)
    times = int(np.log2(length))
    solution = np.zeros((times+1,length))
    solution[0] = step_data
    for i in range(0,times):
        for j in range(0,2 ** (times-i),2):
            solution[i+1][int(j/2)] = (arithmetic_mean(solution[i][j],solution[i][j+1]))
        for j in range(0, 2 ** (times - i), 2):
            for k in range(i,times):
                smooth = smooth_mean(solution[i][j], solution[i][j + 1])
                solution[k+1][int (2 ** (times-i- 1)  + j/2)] = smooth if threshold <= smooth else 0
    return np.array(solution)


test_data = (96, 84, 92, 76, 28, 40, 32, 12, 48, 52, 80, 72, 24, 36, 36, 16)
print(discrete_wavelet_transformation(test_data,5))
test_data = (152, 228, 148, 176, 192, 220, 200, 32)
print(discrete_wavelet_transformation(test_data,30))