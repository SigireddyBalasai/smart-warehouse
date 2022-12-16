from dependencies import *
import numpy as np


class linear_regr:
    def __init__(self, csv_file, var1, var2):
        self.c2 = None
        self.c = None
        self.m = None

        # data_to_use(csv_file)
        data = valuen(csv_file, var1, var2)
        timestamp = list(map(float, data[0]))
        price = list(map(float, data[1]))
        self.timestamp = timestamp
        self.csv_file = csv_file
        self.price = price
        x = np.array(timestamp)
        y = np.array(price)
        n = len(timestamp)
        self.n = n
        mean_x = np.mean(np.array(timestamp))
        mean_y = np.mean(np.array(price))
        ss_xy = np.sum(y * x) - n * mean_y * mean_x
        ss_xx = np.sum(x * x) - n * mean_x * mean_x
        self.ss_xy = ss_xy
        self.ss_xx = ss_xx
        self.price = price
        self.mean_x = mean_x
        self.mean_y = mean_y
        self.timestamp = timestamp

    def test(self):
        ss_xy = self.ss_xy
        ss_xx = self.ss_xx
        mean_x = self.mean_x
        mean_y = self.mean_y
        timestamp = self.timestamp
        n = self.n
        m = ss_xy / ss_xx
        c = mean_y - m * mean_x
        yi = list()
        for i in range(0, n):
            d = (m * timestamp[i] + c)
            yi.append(d)
            return [m, c, n]


def linear_answer(csv_file, var1, var2):
    ok = linear_regr(csv_file, var1, var2).test()
    m = ok[0]
    c = ok[1]
    n = ok[2]
    yi = list()
    data = valuen(csv_file, var1, var2)
    timestamp = list(map(float, data[0]))
    price = list(map(float, data[1]))
    for i in range(0, n):
        d = (m * timestamp[i] + c)
        yi.append(d)
    return [timestamp, yi]
