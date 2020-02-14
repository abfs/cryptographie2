#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 09:18:07 2020

@author: alaeddine.ben-fradj
"""

def compter_occurence (caractere, chaine):
    compteur = 0
    g= caractere
    for caractere in chaine:
        if caractere == g:
            compteur += 1
    return compteur

"""
test pour la question 1
"""
chaine='bonjour'
print(compter_occurence('k',chaine))

"""
question 2
"""

def compter_mots(chaine):
    compteur=1
    chaine_vide=''
    if chaine == chaine_vide:
        return 0
    else:
        # dans ce cas la chaine n'est pas vide
        caractere_precedent = chaine[0]
        for i in range(1, len(chaine)):
            if chaine[i] == ' ' and caractere_precedent != ' ':
                compteur += 1
            caractere_precedent = chaine[i]    
    return compteur

"""
test pour la question 2
"""

chaine='bonjour bonjour estelle bla'
print(compter_mots(chaine))

"""
qeustion 3
"""

def compter_occurences_mot(mot, chaine):
    compteur=0
    for i in chaine.split(' '):
        if i == mot:
            compteur += 1
    return compteur

"""
test pour la question 3
"""

print(compter_occurences_mot('bonjour',chaine))
            
"""
question 4
"""

def substituer():
    
    chaine = 'bonjour estelle buenos dias '
    liste = list(chaine)
    liste[4]= 'z'
    chaine = ''.join(liste)
    print(chaine)

substituer()

"""
question 5
"""

def substituer_mot(mot,remplacement,chaine):
    
    compteur=0
    liste=chaine.split(' ')
    for i in range(len(liste)):
        if liste[i] == mot:
            liste[i]= remplacement
            compteur += 1
    chaine=' '.join(liste)
    return compteur,chaine

"""
test question 5
"""

print(substituer_mot('bonjour','voiture','bonjour bonjour bonjour estelle'))

"""
question 6
"""
