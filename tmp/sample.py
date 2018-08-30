# coding: utf-8
# Author: gjwei
import random

n = 10000000
in_circle = 0


for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        in_circle += 1

    if (i + 1) % 100000 == 0:
        print(in_circle / (i + 1) * 4)