# -*- coding:latin-1 -*-
# Imports :
from random import randrange
from math import ceil
# Declaration de variables :
numero=-1
solde=1000
mise=0
resultat=0
genre=""
gagnant=0
# Fonctions :
def pair_impair(arg):
    resultat=arg%2
    if resultat==0:
        genre="pair"
    if resultat==1:
        genre="impair"
    return genre
# Introduction au jeu :
print("\t\t\tJeu de la roulette :")
print("Vous devez miser minimum 2 euros sur un nombre entre 0 et 49\nSolde :",solde,"euros")
 
# Choix du nombre sur le quel miser :
while numero<0 or numero>49:
    numero=input("Choix du numero sur le quel vous voulez miser : ")
    try:
        numero=int(numero)
    except ValueError:
        print("Vous n'avez pas saisi de nombre correct !")
        numero=0
        continue
    if numero<0:
        print("Vous ne pouvez pas choisir de nombre inferieur a 0 !")
    if numero>49:
        print("Vous ne pouvez pas choisir de nombre superieur a 49 !")
    if numero>=0 and numero<=49:
        pair_impair(numero)
        print("Vous avez joue sur le numero",numero,"et c'est un nombre",genre,"!")
 
# Choix de la mise :
while mise<2 or mise>solde:
    mise=input("Mise : ")
    try:
        mise=int(mise)
    except ValueError:
        print("Vous n'avez pas saisi de nombre correct !")
        mise=0
        continue
    if mise<2:
        print("Vous ne pouvez pas miser en dessous de 2 euros !")
    if mise>solde:
        print("Vous n'avez que",solde,"euros, vous ne pouvez pas miser",mise,"euros !")
    if mise>2 and mise<solde:
        print("Vous avez mise",mise,"euros sur le numero",numero,"qui est",genre,"!")
input("Appuyez sur une touche pour lancer la roulette !")
gagnant=randrange(50)
print("Le numero gagnant est le",gagnant)
print(mise,"sur",numero)
input()