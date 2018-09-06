# coding: utf-8
import re


def sub_blanks(s):
    return re.sub(' ', r'%20', s)


if __name__ == '__main__':
    print(sub_blanks('fawe  erawer'))