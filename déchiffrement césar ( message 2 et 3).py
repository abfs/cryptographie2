# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:21:12 2020

@author: etudiant
"""

with open('message3.txt', 'r', encoding="utf8") as f:
    message = f.read()

def decaler(caractere, decalage):
    nombre_caractere = ord(caractere)
    decale_voulu = nombre_caractere + decalage
    lettre_obtenu = chr(decale_voulu)
    
    return lettre_obtenu


def frequence(texte):
    
    dictionnaire_de_frequence = {}
    for i in range(len(texte)):
        if texte[i] in dictionnaire_de_frequence :
            dictionnaire_de_frequence[texte[i]] += 1
        else:
            dictionnaire_de_frequence[texte[i]] = 1

    
    return dictionnaire_de_frequence


def caractere_plus_frequent(texte):
    
     dictionnaire = frequence(texte)
     j=0
     for i in dictionnaire:
         if dictionnaire[i] >= j:
             plusgrand = dictionnaire[i]
             j= dictionnaire[i]
             caractere_le_plus = i
    
    
     return caractere_le_plus
 
print(caractere_plus_frequent("voituree")) 
print(caractere_plus_frequent(message))

def decalage(chaine):
    
    lettre = caractere_plus_frequent(chaine)
    cle_cesar = ord(' ')-ord(lettre)
    
    return cle_cesar


def chiffrement_cesar(chaine,nombre):
    message_codée = ''
    decalage = nombre
    for c in chaine :
        lettre_obtenu= decaler(c,decalage)
        message_codée= message_codée + lettre_obtenu
    return message_codée

def dechiffrement_de_cesar(chaine):
    cle = decalage(chaine)
    texte = chiffrement_cesar(chaine,cle)
    return texte
    
print(dechiffrement_de_cesar(message))