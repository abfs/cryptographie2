#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:08:28 2020

@author: alaeddine.ben-fradj
"""

"""
message 1
"""
import os
# […]
with open('message 1.txt', 'r') as file:
    # on fait des choses avec le fichier
    message = file.read() # chaîne de caractère avec le contenu du fichier
    # bla
# à partir d'ici, le fichier est fermé
 
    
def compter_occurence (caractere, chaine):
    compteur = 0
    g= caractere
    for caractere in chaine:
        if caractere == g:
            compteur += 1
    return compteur

compter_occurence()