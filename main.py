import csv
import matplotlib.pyplot as plt
import numpy as np


def statistics(data: list) -> tuple:
    np_data = np.array(data)

    mean = np.mean(np_data)
    dispersion = np.var(np_data)
    variance = np.std(np_data)

    return mean, dispersion, variance


def read(file: str):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        close = []
        for row in csv_reader:
            if line_count != 0:
                close.append(float(row[7]))
            line_count += 1
        return close


def solve():
    # read the data
    eurrub = read('EURRUB_200101_220131.csv')
    usdrub = read('USDRUB_200101_220131.csv')

    # get the statistical values
    print('1: ')
    print('Валюта ; Mathematical Expectation ; Dispersion ; Variance (СКО)')
    print('EUR/RUB', statistics(eurrub))
    print('USD/RUB', statistics(usdrub))

    # plot with matplotlib
    print('\n\n2: \n')
    # EUR/RUB
    plt.subplot(2, 1, 1)
    plt.title('EUR / RUB валют')
    plt.xlabel('Валют')
    plt.ylabel('Частота')
    plt.hist(eurrub, bins=5)
    plt.hist(eurrub, bins=7)
    plt.hist(eurrub, bins=10)

    # USD/RUB
    plt.subplot(2, 1, 2)
    plt.title('USD / RUB валют')
    plt.xlabel('Валют')
    plt.ylabel('Частота')
    plt.hist(np.array(usdrub), bins=5)
    plt.hist(np.array(usdrub), bins=7)
    plt.hist(np.array(usdrub), bins=10)

    # plot display
    plt.tight_layout()
    plt.show()

    # Covariance
    print('\n\n3.')
    cov = np.cov(eurrub, usdrub)[0][1]
    print(f'\nКовариация: {cov}')

    # Correlation
    corr = np.corrcoef(eurrub, usdrub)[0][1]
    print(f'Коэффициент Корреляция: {corr}')


if __name__ == "__main__":
    solve()
