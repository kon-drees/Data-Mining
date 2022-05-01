import numpy as np


data_set = [[1, 2, 4], [1, 2, 4], [1, 2, 3]]
data_set2 = [["a", "2", "4"], ["1", "2", "4"], ["1", "2", "3"]]


# calculate the support supp(A => B) in a transactions list
def supp(a, b, transactions):
    count = 0
    for transaction in transactions:
        if a in transaction and b in transaction:
            count += 1
    return count / len(transactions)


# calculate the support supp(A) in a transactions list
def supp_count(a, transactions):
    count = 0
    for transaction in transactions:
        if a in transaction:
            count += 1
    return count / len(transactions)


# calculate the confidence conf(A => B) in a transactions list
def conf(a, b, transactions):
    count_a = 0
    count_ab = 0
    for transaction in transactions:
        if a in transaction:
            count_a += 1
            if b in transaction:
                count_ab += 1
    return count_ab / count_a


print(supp("1", "4", data_set2))
print(conf("1", "4", data_set2))
