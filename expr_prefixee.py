#! /usr/bin/python3.6
# coding: utf-8

__author__ = "Derrien Tanguy"

def estNombre(t):
	return t[0] == int 

def valeur(t):
	if estNombre(t):
		return t[1]
	else:
		return None

def caractere(t):
	if not estNombre(t):
		return t[2]
	else:
		return None

def creerTerme(e):
	return [int, e, None]

def creerOp(op):
	return [str, None, op]

def afficher(p):
	res = []
	for t in p:
		if estNombre(t):
			res.append(t[1])
		else:
			res.append(t[2])
	print(res)

def evaluate(expr):
	pile = []
	for t in expr:
		if not estNombre(t):
			pile.append(t)
		else:
			suivant = t
			while len(pile) > 0 and estNombre(pile[-1]):
				res = eval(str(valeur(pile.pop())) + caractere(pile.pop()) + str(valeur(suivant)))
				suivant = creerTerme(res)
			pile.append(suivant)
		afficher(pile)
	print(valeur(pile[-1]))
