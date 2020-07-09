#! /usr/bin/python3.6
# coding: utf-8

__author__ = "Derrien Tanguy"

from expr_prefixee import *

# 2 x 3 + 12 + 8 = 26
print('2 x 3 + 12 + 8')
evaluate([creerOp('+'), creerOp('*'), creerTerme(2), creerTerme(3), creerOp('+'), creerTerme(12), creerTerme(8)])
print()
# (4 + 5 + 6) x 3 = 45
print('(4 + 5 + 6) x 3')
evaluate([creerOp('*'), creerTerme(3), creerOp('+'), creerOp('+'), creerTerme(4), creerTerme(5), creerTerme(6)])
print()
# (3 + 4) x 5 = 35
print('(3 + 4) x 5')
evaluate([creerOp('*'), creerTerme(5), creerOp('+'), creerTerme(3), creerTerme(4)])
print()
# 4 x 5 + 3 = 23
print('4 x 5 + 3')
evaluate([creerOp('+'), creerTerme(3), creerOp('*'), creerTerme(4), creerTerme(5)])
print()
# 4 + 5 + 3 = 12
print('4 + 5 + 3')
evaluate([creerOp('+'), creerTerme(3), creerOp('+'), creerTerme(4), creerTerme(5)])
print()
# (3 x 4 - 12) x (-1 + 2 x 6 - (-4)) = 0
print('(3 x 4 - 12) x (-1 + 2 x 6 - (-4))')
evaluate([creerOp('*'), creerOp('-'), creerOp('+'), creerTerme(-1), creerOp('*'), creerTerme(2), creerTerme(6), creerTerme(-4), creerOp('-'), creerOp('*'), creerTerme(3), creerTerme(4), creerTerme(12)])
