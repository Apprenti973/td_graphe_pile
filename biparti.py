#! /usr/bin/python3.6
# coding: utf-8

__author__ = "Derrien Tanguy"

from collections import deque
from random      import choice

def biparti(G):
	"""
	Renvoie True si le graphe G est biparti. Dans ce cas, renvoie également les
	ensembles "rouge" et "bleu" de sommets disjoints.
	Renvoie False si le graphe n'est pas biparti. Dans ce cas, renvoie également
	"cycle" un cycle impair du graphe G.
	Entree :
	G (dictionnaire) : G[sommets] = [ voisin1, voisin2, etc.]  
	Sortie :
	(True, rouge, bleu | False, cycle)
	"""
	# file vide 
	d = deque()

	# les sommets du graphe saont rangés par couleur
	rouge, bleu = [], []
	
	# dictionnaire des sommets déjà coloriés
	colories = {}
	
	# dictionnaire des pères des sommets coloriés utilisé pour le cycle impair
	peres = {}
	
	# le sommet de départ du parcours est choisi aléatoirement
	sommet = choice(list(G.keys()))

	# racine servira à trouver le cycle impair
	racine = sommet
	# racine est son propre père
	peres[sommet] = sommet

	d.append(sommet)

	# sommet est colorié en bleu ; 1 --> bleu et 0 --> rouge
	colories[sommet] = 1
	bleu.append(sommet)

	# tant que la file n'est pas vide
	while len(d):

		# pour chaque voisin de sommet	
		for voisin in G[sommet]:

			# on vérifie que le voisin n'a pas déjà été colorié
			if voisin not in colories:
				peres[voisin] = sommet
				d.append(voisin)
				
				# si sommet est bleu (1), voisin est (1 + 1) % 2 = 0 = rouge et
				# si sommet est rouge (0), voisin est (0 + 1) % 2 = 1 = bleu
				colories[voisin] = (colories[sommet] + 1) % 2

				# si voisin est ajacent à un sommet de même couleur
				# alors le graphe n'est pas biparti
				couleur = (rouge if not colories[voisin] else bleu)
				couleur.append(voisin)
				for vertice in couleur:
					if vertice in G[voisin]:

						# recherche d'un cycle dont une arête est
						# vertice -- voisin (nécessairement impair...)
						c = cycle(G, racine, peres, vertice, voisin)
						return False, c
		d.popleft()
		if len(d):
			sommet = d[0]
	return True, bleu, rouge


def cycle(G, racine, peres, a, b):
	"""
	Renvoie un cycle contenant le lien b - a en cherchant le plus proche ancêtre
	commun de a et de b : ppac. Le cycle sera donc b -...- ppac -...- a - b
	Entrées :
	G (dictionnaire) : graphe en entrée de la fonction biparti
	racine : noeud de départ du parcours BFS de G
	peres (dictionnaire) : peres des sommets coloriés dans la fonction biparti
	a, b : sommets adjacents de même couleur
	Sortie :
	cycle (liste) 
	"""
	marques, cycle = {}, []
	marques[racine] = True
	
	# une fois construite, chaine_a aura pour extrémités a et racine
	chaine_a = [a]
	
	# on marque tous les ancêtres de a jusqu'à la racine et on construit
	# chaine_a en même temps
	noeud = a
	while noeud != racine:
		marques[noeud] = True
		noeud = peres[noeud]
		chaine_a.append(noeud)
	
	# une fois construite, chaine_b aura pour extrémités b et ppac
	chaine_b = [b]
	
	# on remonte les ancêtres de b jusqu'à en trouver un marqué : le ppac et on
	# construit chaine_b en même temps
	noeud = b
	while noeud not in marques:
		noeud = peres[noeud]
		chaine_b.append(noeud)
	
	# cycle = [b -...- ppac -...- a]
	cycle = chaine_b + [chaine_a[i] for i in range(chaine_a.index(chaine_b[len(chaine_b)-1]))][::-1]
	
	# retourner [b -...-ppac -...- a - b]
	return cycle + [b]
