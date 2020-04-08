# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:05:39 2020

@author: etudiant
"""

def decaler(caractere, decalage):
    nombre_caractere = ord(caractere)
    decale_voulu = nombre_caractere + decalage
    lettre_obtenu = chr(decale_voulu)
    
    return lettre_obtenu

"""
def chiffrement_cesar(chaine,nombre):
    message_codée = ''
    decalage = nombre
    for c in chaine :
        lettre_obtenu= decaler(c,decalage)
        message_codée= message_codée + lettre_obtenu
    return message_codée
"""

"""
question 1 
"""

def vigenere(message,cle):
    
    message_chiffré =''
    if len(message) == len(cle):
        print(message)
        for i in range(len(message)):
                decalage = cle[i]
                print(cle[i])
                lettre_obtenu = decaler(message[i],decalage)
                message_chiffré = message_chiffré + lettre_obtenu
    
    else :
        cle_complete = cle
        while len(message) != len(cle_complete):
            for i in range(len(cle)):
                cle_complete.append(cle[i])
                if len(message) == len(cle_complete):
                    break
            
        for i in range(len(message)):
                decalage = cle_complete[i]
                print(cle_complete[i])
                lettre_obtenu = decaler(message[i],decalage)
                message_chiffré = message_chiffré + lettre_obtenu
    
    return message_chiffré

        
print(vigenere('monmessa',[1,4,3]))


def dechiffrement_vigenere(message,cle):
    
    message_dechiffre=''
    #cle_dechifrement = (c,cle)-(2*clé)
    if len(message) == len(cle):
        print(message)
        for i in range(len(message)):
                decalage = cle[i]-(2*cle[i])
                print(cle[i])
                lettre_obtenu = decaler(message[i],decalage)
                message_dechiffre = message_dechiffre + lettre_obtenu
    else :
        cle_complete = cle
        while len(message) != len(cle_complete):
            for i in range(len(cle)):
                cle_complete.append(cle[i])
                if len(message) == len(cle_complete):
                    break
            
        for i in range(len(message)):
                decalage = cle_complete[i]-(2*cle_complete[i])
                print(cle_complete[i])
                lettre_obtenu = decaler(message[i],decalage)
                message_dechiffre = message_dechiffre + lettre_obtenu
    
    
    return message_dechiffre

print(dechiffrement_vigenere('nsqnivte',[1,4,3]))


"""
question 3
"""
def frequence(texte):
    
    dictionnaire_de_frequence = {}
    for i in range(len(texte)):
        if texte[i] in dictionnaire_de_frequence :
            dictionnaire_de_frequence[texte[i]] += 1
        else:
            dictionnaire_de_frequence[texte[i]] = 1

    
    return dictionnaire_de_frequence

print(frequence('bienvenue'))

"""
question 4
"""


def caractere_plus_frequent(texte):
    
     dictionnaire = frequence(texte)
     for i in dictionnaire:
         j =dictionnaire.values()
         caractere_le_plus = j[0]
         if j >= dictionnaire[i]:
             caractere_le_plus=dictionnaire[i]
         else:
             break
             
             
    
     return caractere_le_plus


print(caractere_plus_frequent('anticonstitutionnellement'))
    

    

    
    
    



















