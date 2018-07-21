# coding: utf-8
# Author: gjwei

def sort_map(hm):
    from operator import itemgetter
    sorted(hm.items(), key=lambda x: x[1], reverse=True)

