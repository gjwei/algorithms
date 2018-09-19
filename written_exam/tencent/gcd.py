from functools import reduce
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_seq(seq):
    return reduce(lcm, seq)


def solution(n):
    m = n + 1
    l1 = lcm_seq(list(range(1, m + 1)))
    l2 = m

    while l1 != l2:
        m += 1
        l1 = lcm(l1, m)
        l2 = lcm(l2, m)

    return m


if __name__ == '__main__':
    n = int(input())
    r = solution(n)
    print(r)
