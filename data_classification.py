import numpy as np


def information_gain(p, n):
    if p == 0 or n == 0:
        return 0
    return -p/(p+n)*np.log2(p/(p+n))-n/(p+n)*np.log2(n/(p+n))


def split_info(*args):
    sum = 0
    for elem in args:
        sum += elem
    split = 0
    for elem in args:
        if elem == 0:
            pass
        else:
            split -= elem/sum*np.log2(elem/sum)
    return split


i_e = information_gain(4, 2)
i_sol1 = i_e - (2/6*information_gain(1, 1)+2/6*information_gain(0, 1)+2/6*information_gain(1, 1))
i_sol2 = i_e - (2/6*information_gain(2, 0)+3/6*information_gain(0, 1)+1/6*information_gain(1, 0))
i_sol3 = i_e - (2/6*information_gain(2, 0)+1/6*information_gain(0, 1)+3/6*information_gain(1, 0))
i_sol4 = i_e - (8/12*information_gain(3, 1)+4/12*information_gain(2, 2))

i_split1 = split_info(2, 2, 2)
i_split2 = split_info(2, 3, 1)
i_split3 = split_info(2, 1, 3)
i_split4 = split_info(4, 4, 4)

i_gain_ratio1 = i_sol1 / i_split1
i_gain_ratio2 = i_sol2 / i_split2
i_gain_ratio3 = i_sol3 / i_split3
i_gain_ratio4 = i_sol4 / i_split4


print(i_e)
print(i_sol1)
print(i_sol2)
print(i_sol3)
print(i_sol4)
print(i_split1)
print(i_split2)
print(i_split3)
print(i_split4)
print(i_gain_ratio1)
print(i_gain_ratio2)
print(i_gain_ratio3)
print(i_gain_ratio4)