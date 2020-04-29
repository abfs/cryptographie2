# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:37:02 2020

@author: etudiant
"""

with open('message4.txt', 'r', encoding="utf8") as f:
    message4 = f.read()
    
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
    global caractere_le
    dictionnaire = frequence(texte)
    j=0
    for i in dictionnaire:
        if dictionnaire[i] >= j:
             plusgrand = dictionnaire[i]
             j= dictionnaire[i]
             caractere_le = i
    
    
    return caractere_le
#%%
     
def decalage(chaine):
    """
    fonction permettant d'avoier la clé en sortie
    """
    lettre = caractere_plus_frequent(chaine)
    cle_cesar = ord(' ')-ord(lettre)
    
    return cle_cesar

def chiffrement_cesar(chaine,nombre):
    """
    fonction qui chiffre un texte avec la méthode de césar
    entré : texte et la clé
    sortie : texte crypté
    """
    message_codée = ''
    decalage = nombre
    for c in chaine :
        lettre_obtenu= decaler(c,decalage)
        message_codée= message_codée + lettre_obtenu
    return message_codée


def dechiffrement_de_cesar(chaine):
    """
    fonction qui dechiffre un texte à partir d'un texte crypté
    entré : texte crypté
    sortie : texte decrypté
    """
    cle = decalage(chaine)
    texte = chiffrement_cesar(chaine,cle)
    return texte
    
#%%

def déchiffrement_message4(message):
    """
    fonction permettant de déchiffrer le message avec une partie qui permet de séparer les lettres en positions paires
    et impaires
    entre : le texte
    sortie : le texte decrpyté
    """
    message_decrypté =''
    message_paire =''
    message_impaire =''
    for i in range(len(message)) :
        if (i % 2) == 0:
            message_paire = message_paire + message[i]
        else:
            message_impaire = message_impaire + message[i]
    """
    cette partie est plus classique pour le déchiffrement avec une clé de césar
  
    """
    message_paire_decrypte = dechiffrement_de_cesar(message_paire)
    message_impaire_decrypte = dechiffrement_de_cesar(message_impaire)
    for i in range(len(message_paire_decrypte)):
        message_decrypté += message_paire_decrypte[i] + message_impaire_decrypte[i]
    
    return message_decrypté

print(déchiffrement_message4(message4))
    