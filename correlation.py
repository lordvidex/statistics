import numpy as np

x = [1, 2, 3, 4, 5]
y = [10, 12, 14, 16, 17]


def mean(l):
    summ = 0
    for g in l:
        summ += g
    return summ / len(l)

# returns c and m for y=c+mx
def solve(x, y):
    numerator = mean(np.multiply(x, y)) - mean(x) * mean(y)
    denominator = mean([pow(temp, 2) for temp in x]) - mean(x) * mean(x)
    b = numerator / denominator
    a = mean(y) - b * mean(x)
    # print(b)
    # print(a)

    _y = [a + b * _x for _x in x]

    # coefficient
    coef_num = 0
    for i in range(len(y)):
        diff = y[i] - _y[i]
        coef_num += (diff * diff)
    coef_den = sum([pow((yi - a), 2) for yi in y])

    # print(x)
    # print(y)
    # print(_y)
    #
    # print(1 - coef_num / coef_den)
    return a, b
