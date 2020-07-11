#! /usr/bin/python3.6
# coding: utf-8

__author__ = "Derrien Tanguy"

from biparti import *

G, H, I, J = {}, {}, {}, {}

# graphe non biparti ===> https://drive.google.com/file/d/1Hki5Rg9qtRSAJNqR6u96T15_M2hH2UW6/view?usp=sharing
G[0]  = [6, 7]
G[1]  = [3, 8, 10]
G[2]  = [7, 9]
G[3]  = [1, 4]
G[4]  = [3, 5, 6]
G[5]  = [4, 10]
G[6]  = [0, 4]
G[7]  = [0, 2, 8]
G[8]  = [1, 7, 9, 10]
G[9]  = [2, 8]
G[10] = [1, 5, 8]

# graphe non biparti ===> https://drive.google.com/file/d/1EU508ySccDgaRsTaMAiV-wfmmqqv5i2Q/view?usp=sharing
H[0]  = [1, 4, 5, 7]
H[1]  = [0, 2, 3, 4]
H[2]  = [1, 4]
H[3]  = [1, 6, 9]
H[4]  = [0, 1, 2]
H[5]  = [0, 7, 10]
H[6]  = [3, 9]
H[7]  = [0, 5, 8, 10, 11]
H[8]  = [7, 10, 12]
H[9]  = [3, 6]
H[10] = [5, 7, 8]
H[11] = [7]
H[12] = [8]

# graphe non biparti ===> https://drive.google.com/file/d/1SDzc8uznY09_lsQNxIBrBcys52Cq-WfF/view?usp=sharing
I['A'] = ['B', 'D']
I['B'] = ['A', 'E', 'F', 'H']
I['C'] = ['D', 'E']
I['D'] = ['A', 'C', 'G']
I['E'] = ['B', 'C', 'F']
I['F'] = ['B', 'E', 'H']
I['G'] = ['D', 'H']
I['H'] = ['B', 'F', 'G']

# graphe de la question 5
J['v1']  = ['v2', 'v3']
J['v2']  = ['v1', 'v4', 'v5']
J['v3']  = ['v1', 'v5', 'v10']
J['v4']  = ['v2', 'v6']
J['v5']  = ['v2', 'v3', 'v6']
J['v6']  = ['v4', 'v5', 'v7']
J['v7']  = ['v6', 'v8']
J['v8']  = ['v7', 'v9', 'v10']
J['v9']  = ['v8']
J['v10'] = ['v3', 'v8']

for graphe in G, H, I, J:
	print(biparti(graphe))
