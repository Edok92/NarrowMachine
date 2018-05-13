# -*- coding: utf-8 -*-
import csv
from itertools import groupby

# ATTENTION ::::: les phrases twitter doivent être convertis en UTF-8 

def delete_accent(element):
        """ supprime les accents des tweets """
        accents = { 'a': ['à', 'ã', 'á', 'â'],
                    'e': ['é', 'è', 'ê', 'ë'],
                    'i': ['î', 'ï'],
                    'u': ['ù', 'ü', 'û'],
                    'o': ['ô', 'ö'] }
        for (char, accented_chars) in accents.iteritems():
            for accented_char in accented_chars:
                element = element.replace(accented_char, char)
        return element
        
def delete_ponctuation(element):
    """ supprime la ponctuation des tweets """
    ponctuation = { '': ['.'] }
    for (char, accented_chars) in ponctuation.iteritems():
        for accented_char in accented_chars:
            element = element.replace(accented_char, char)
    return element
        
def delete_numbers(element):
    """ supprime les nombres des tweets """
    numbers = { '': ['1', '2', '3', '4', '5', '6', '7', '8', '9'] }
    for (char, all_numbers) in numbers.iteritems():
            for number in all_numbers:
                element = element.replace(number, char)
    return element
    
def delete_repetitive_chars(element):
    """ supprime les caractères répétés successivement """
    final = ""
    for word in element.split():
        word = ''.join([x for x,y in groupby(word) if sum(1 for i in y)<2])
        final += word
    
    return str(final)
            
    
#Dico = [["mot", "enthousiaste", "content", "neutre", "triste", "colere"]]        
Dico = [["mot", 0, 0, 0, 0, 0, 0]]

# On stocke les valeurs du dictionnaire
i = 0
exist = 0
with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        words = row['phrase'].split()
        for word in words:
            exist = 0
            for line in Dico:
                # si le mot existe
                if line[0] == word:
                    enthousiaste = line[1]
                    content = line[2]
                    neutre = line[3]
                    triste = line[4]
                    colere = line[5]
                    if row['sentiment'] == "enthousiaste":
                        Dico[i][1] += 1
                        enthousiaste += 1
                    if row['sentiment'] == "content":
                        Dico[i][2] += 1
                        content += 1
                    if row['sentiment'] == "neutre":
                        Dico[i][3] += 1
                        neutre += 1
                    if row['sentiment'] == "triste":
                        Dico[i][4] += 1
                        triste += 1
                    if row['sentiment'] == "colere":
                        Dico[i][5] += 1
                        colere += 1
                    Dico[i][6] += 1
                    i += 1
                    exist = 1
            # le mot n'existe pas encore donc on l'ajoute
            if exist == 0:
                enthousiaste = 0
                content = 0
                neutre = 0
                triste = 0
                colere = 0
                if row['sentiment'] == "enthousiaste":
                    enthousiaste += 1
                if row['sentiment'] == "content":
                    content += 1
                if row['sentiment'] == "neutre":
                    neutre += 1
                if row['sentiment'] == "triste":
                    triste += 1
                if row['sentiment'] == "colere":
                    colere += 1
                
                # on supprime les nombres
                word = delete_numbers(word)
                # on supprime les caractères répétitifs 
                word = delete_repetitive_chars(word)
                # on supprime la ponctuation
                word = delete_ponctuation(word)
                
                new = [delete_accent(word), enthousiaste, content, neutre, triste, colere, 1]
                Dico.append(new)

with open('dictionnaire.csv', 'w') as csvfile:
    fieldnames = ['mot', 'enthousiaste', 'content', 'neutre', 'triste', 'colere', 'appearance']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for line in Dico:
        writer.writerow({'mot': line[0], 'enthousiaste': line[1], 'content': line[2], 'neutre': line[3], 'triste': line[4], 'colere': line[5], 'appearance': line[6]})