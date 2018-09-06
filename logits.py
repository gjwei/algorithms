# coding: utf-8
# Author: gjwei

import math

def logits(p):
    return math.log(p / (1 - p))

print(logits(0.9) - logits(0.8))
print(logits(0.15) - logits(0.05))
