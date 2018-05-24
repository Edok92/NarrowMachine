# -*- coding: utf-8 -*-
import csv
import re
import connect
from itertools import groupby

# ATTENTION ::::: les phrases twitter doivent être convertis en UTF-8 

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
        
def delete_ponctuation(element):
    """ supprime la ponctuation des tweets """
    ponctuation = { '': ['.'] }
    for (char, accented_chars) in ponctuation.items():
        for accented_char in accented_chars:
            element = element.replace(accented_char, char)
    return element
        
def delete_numbers(element):
    """ supprime les nombres des tweets """
    numbers = { '': ['1', '2', '3', '4', '5', '6', '7', '8', '9'] }
    for (char, all_numbers) in numbers.items():
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

def delete_url(element):
    """ supprime les mots contenant une adresse http ou https """
    found = re.search(r'http', element)
    if found:
       return ''  
    else:
        return element
        
def delete_tag(element):
    """ supprime les mots avec @ (correspondant aux tags """
    found = re.search(r'@', element)
    if found:
       return ''
    else:
        return element
    
def delete_hashtag(element):
    """ supprime les mots avec @ (correspondant aux tags """
    found = re.search(r'#', element)
    if found:
       return element.replace('#' , '')
    else:
        return element
            
    
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
            #word = delete_repetitive_chars(word)
            # on supprime la ponctuation
            word = delete_ponctuation(word)
                
            #new = [delete_accent(word), enthousiaste, content, neutre, triste, colere, 1]
            #Dico.append(new)
            word = delete_url(word)
            word = delete_tag(word)
            #word = delete_hashtag(word)
            word = delete_accent(word)
            
            conn = connect.connect()
            cur = conn.cursor()
        
            print(word)
            #print 'ResultCount = %d' % len(rows)
            
            cur.execute('select count(*) from dico where mot = %s;',[word])
            result = cur.fetchone()
            nbrRows = result[0]
            print(nbrRows)
            
            if nbrRows == 0: #si le mot n'existe pas
                cur.execute("INSERT INTO dico (mot, enthousiaste, content, neutre, triste , colere , appearance) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        , (word,enthousiaste,content,neutre,triste,colere, 1))
                conn.commit()
            else :
                cur.execute('select * from dico where mot = %s;',[word])
                rows = cur.fetchone()
                
                enthousiaste += rows[1]#'enthousiaste'
                content += rows[2]#'content'
                neutre += rows[3]#'neutre'
                triste += rows[4]#'triste'
                colere += rows[5]#colere
                appearance = rows[6] + 1 # 5 = appearance
                
                cur.execute("UPDATE dico SET enthousiaste = %s, content = %s, neutre = %s, triste = %s, colere = %s, appearance = %s WHERE mot = %s"
                        , (enthousiaste,content, neutre,triste,colere, appearance, word))
                conn.commit()
                    
                
with open('dictionnaire.csv', 'w') as csvfile:
    fieldnames = ['mot', 'enthousiaste', 'content', 'neutre', 'triste', 'colere', 'appearance']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for line in Dico:
        writer.writerow({'mot': line[0], 'enthousiaste': line[1], 'content': line[2], 'neutre': line[3], 'triste': line[4], 'colere': line[5], 'appearance': line[6]})