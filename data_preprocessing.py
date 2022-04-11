import numpy as np


def arithmetic_mean(x, y):
    return (x+y)/2


def smooth_mean(x, y):
    return x - arithmetic_mean(x, y)


# iterative solution for a wavelet_transformations
def discrete_wavelet_transformation(data, threshold):
    step_data = list(data)
    if len(step_data) % 2 != 0:
        step_data.append(0)
    length = len(step_data)
    times = int(np.log2(length))
    solution = np.zeros((times+1, length))
    solution[0] = step_data
    for i in range(0,times):
        for j in range(0,2 ** (times-i), 2):
            solution[i+1][int(j/2)] = (arithmetic_mean(solution[i][j], solution[i][j+1]))
        for j in range(0, 2 ** (times - i), 2):
            for k in range(i, times):
                smooth = smooth_mean(solution[i][j], solution[i][j + 1])
                solution[k+1][int(2 ** (times-i-1) + j/2)] = smooth if threshold <= smooth else 0
    return np.array(solution)


test_data = (96, 84, 92, 76, 28, 40, 32, 12, 48, 52, 80, 72, 24, 36, 36, 16)
print(discrete_wavelet_transformation(test_data,5))
test_data = (152, 228, 148, 176, 192, 220, 200, 32)
print(discrete_wavelet_transformation(test_data,30))


# an iterative solution for a progressive logarithmic tilted time function
def progressive_log_tilted_time_frame(timestamp, bk, b_max):
    timetable = [[0 for _ in range(bk)] for _ in range(b_max+1)]
    i_max = int(np.ceil(np.log2(timestamp)))
    container = 0
    for t in range(1, timestamp+1):
        if(np.log2(t)-bk <= b_max) and (b_max <= np.log2(t)):
            for i in range(0, i_max):
                if((t%(2**i)==0) and (t%(2**(i+1))!=0)):
                    container = i
            if (container >= b_max):
                container = b_max
            timetable[container].insert(0, t)
            timetable[container].pop()

    return timetable


def first_change_in_row6():
    timetable = progressive_log_tilted_time_frame(50, 5, 5)
    change = False
    i = 1
    while not change:
        to_check = progressive_log_tilted_time_frame(50+i, 5, 5)
        if timetable[4][0] != to_check[4][0]:
            change = True
        i += 1
    return i+50


print(progressive_log_tilted_time_frame(200, 5, 4))
print(progressive_log_tilted_time_frame(200, 6, 3))
print(progressive_log_tilted_time_frame(50, 5, 5))
print(first_change_in_row6())

