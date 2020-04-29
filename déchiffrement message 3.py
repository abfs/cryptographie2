# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:05:12 2020

@author: etudiant
"""

with open('message3.txt', 'r', encoding="utf8") as f:
    message = f.read()
#%%
def decaler(caractere, decalage):
    """
    fonction permettant de décaler une lettre avec une clé
    entre : caractère et la clé
    sortie : caractère crypté
    """
    nombre_caractere = ord(caractere)
    decale_voulu = nombre_caractere + decalage
    lettre_obtenu = chr(decale_voulu)
    
    return lettre_obtenu

#%%
    
def frequence(texte):
    """
    fonction permettant de classer dans un dictionnaire les lettres et leur nombres d'apparition
    entré : texte
    sortie : dictionnaire avec les lettres utilisées et leurs fréquences 
    """
    
    dictionnaire_de_frequence = {}
    for i in range(len(texte)):
        if texte[i] in dictionnaire_de_frequence :
            dictionnaire_de_frequence[texte[i]] += 1
        else:
            dictionnaire_de_frequence[texte[i]] = 1

    
    return dictionnaire_de_frequence


def caractere_plus_frequent(texte):
     """
     comparaison des lettres du texte et leurs fréquence pour avoir la lettre la plus fréquente en sortie
     entre : texte
     sortie : un caractère
     """
    
     dictionnaire = frequence(texte)
     j=0
     for i in dictionnaire:
         if dictionnaire[i] >= j:
             plusgrand = dictionnaire[i]
             j= dictionnaire[i]
             caractere_le_plus = i
    
    
     return caractere_le_plus
 
#%%

def decalage(chaine):
    """
    fonction permettant d'avoier la clé en sortie
    """
    
    lettre = caractere_plus_frequent(chaine)
    cle_cesar = ord(' ')-ord(lettre)
    
    return cle_cesar


def chiffrement_cesar(texte,nombre):
    """
    fonction qui chiffre un texte avec la méthode de césar
    entré : texte et la clé
    sortie : texte crypté
    """
    
    message_codée = ''
    decalage = nombre
    for c in texte :
        lettre_obtenu= decaler(c,decalage)
        message_codée= message_codée + lettre_obtenu
    return message_codée

def dechiffrement_de_cesar(texte):
    """
    fonction qui dechiffre un texte à partir d'un texte crypté
    entré : texte crypté
    sortie : texte decrypté
    """
    
    cle = decalage(texte)
    texte_decrypte = chiffrement_cesar(texte,cle)
    return texte_decrypte
    
print(dechiffrement_de_cesar(message))