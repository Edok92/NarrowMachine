# -*- coding: utf-8 -*-
import csv 
import connect

Dico = [["mot", 0.0, 0.0, 0.0, 0.0, 0.0, 0]]

# On stocke les valeurs du dictionnaire
def delete_accent(element):
        """ supprime les accents des tweets """
        accents = { 'a': ['à', 'ã', 'á', 'â'],
                    'e': ['é', 'è', 'ê', 'ë'],
                    'i': ['î', 'ï'],
                    'u': ['ù', 'ü', 'û'],
                    'o': ['ô', 'ö']}
        for (char, accented_chars) in accents.items():
            for accented_char in accented_chars:
                element = element.replace(accented_char, char)
        return element

def affiche_resultat(phrase):
    print(phrase)
    words = phrase.split()
    size = len(words)
    result = [0.0, 0.0, 0.0, 0.0, 0.0]
    conn = connect.connect()
    nb = 0
    cur = conn.cursor()
    for word in words:
        word = delete_accent(word)
        cur.execute('select * from dico where mot = %s;',[word])
        rows = cur.fetchone()
        
        if rows is None:
            print("")
            return (result, 0)    
        else:
            print(word)
            appearance = rows[6] #appearance
            
            enthousiaste = rows[1] / appearance #'enthousiaste'
            content = rows[2] / appearance#'content'
            neutre = rows[3] / appearance#'neutre'
            triste = rows[4] / appearance#'triste'
            colere = rows[5] / appearance#colere
    
            result[0] += enthousiaste
            result[1] += content
            result[2] += neutre
            result[3] += triste
            result[4] += colere
        
            result[0] /= size
            result[1] /= size
            result[2] /= size
            result[3] /= size
            result[4] /= size
            
            nb += 1
            return (result, 1)
            
    #if nb > 0 :
    #    return (result, 1)
    #else:
    #    return(result, 0)
    
    #result[0] *= 100
    #result[1] *= 100
    #result[2] *= 100
    #result[3] *= 100
    #result[4] *= 100
    #result[5] *= 100