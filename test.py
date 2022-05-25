import matplotlib.pyplot as plt
import correlation as corr
v = 7
b0 = 0
b1 = 0
r_squared = 0
q = [96 + v, 95 + v, 92 + v, 94 + v, 92 + v, 95 + v, 93 + v, 98 + v, 98 + v, 97 + v, 99 + v, 96 + v, 94 + v, 98 + v, 96 + v, 98 + v]
p = [2,2.3,4.1,3.1,4,2.7,3.6,1, 1.2,1.3,0.7,2,3,0.8,2.1,1]


def solve1():
    global v,p,q
    plt.scatter(p, q)
    plt.show()


def solve2():
    global p, q, b0, b1
    b0, b1 = corr.solve(p, q)
    x = [val for val in p]
    x.sort()
    y = [b0 + b1 * pr for pr in x]

    plt.plot(x, y)
    plt.scatter(x, y)
    plt.title('Graph of q=b0 + b1p')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()


def solve5():
    global q, _y
    _y = [1 if _q > 105 else -1 for _q in q]
    print("Фиктивную перемению: ", _y)


def solve3():
    global q, r_squared
    _q = [b0 + b1 * pr for pr in p]
    numerator = 0
    denominator = 0
    mean = corr.mean(q)
    for i in range(len(q)):
        numerator += pow((q[i] - _q[i]), 2)
    for i in range(len(q)):
        denominator += pow(q[i] - mean, 2)
    r_squared = 1 - numerator/denominator
    return r_squared


def solve4():
    global r_squared, q
    n = len(q)
    return 1 - (1-r_squared)*((n-1)/(n-2))


if __name__ == '__main__':
    print("Question 1 ---- ")
    solve1()
    print("Question 2 ---- ")
    solve2()
    print("Question 3 ---- ")
    solve3()
    print("Question 4 -----")
    print(r_squared)
    print(solve4())
    print("Question 5 ---- ")
    solve5()
