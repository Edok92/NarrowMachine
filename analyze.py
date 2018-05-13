# -*- coding: utf-8 -*-
import csv 

Dico = [["mot", 0.0, 0.0, 0.0, 0.0, 0.0, 0]]

# On stocke les valeurs du dictionnaire
with open('dictionnaire.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        new = [row['mot'], float(row['enthousiaste'])/float(row['appearance']), float(row['content'])/float(row['appearance']), float(row['neutre'])/float(row['appearance']),
              float(row['triste'])/float(row['appearance']), float(row['colere'])/float(row['appearance']), row['appearance']]
        Dico.append(new)
        
phrase = "Le ciel est triste"

result = [0.0, 0.0, 0.0, 0.0, 0.0]
# 0 : enthousiaste
# 1 : content
# 2 : neutre
# 3 : triste
# 4 : colere

words = phrase.split()
size = len(words)
for word in words:
    for i in range(0, len(Dico)):
        if Dico[i][0] == word:
            # (enthousiaste + content) - (triste + colere) > 0.2 => on prend le mot en compte
            # sinon non
            if abs((Dico[i][1] + Dico[i][2]) - (Dico[i][3] + Dico[i][4])) > 0.2:            
                result[0] += float(Dico[i][1]) / float(size)    # enthousiaste
                result[1] += float(Dico[i][2]) / float(size)    # content
                result[2] += float(Dico[i][3]) / float(size)    # neutre
                result[3] += float(Dico[i][4]) / float(size)    # triste
                result[4] += float(Dico[i][5]) / float(size)    # colere
            
print ""
            
print "Présence de sentiments dans la phrase : "
print ""
print phrase
print "Enthousiaste : "
print result[0] * 100, "%" 
print "Content : " 
print result[1] * 100, "%"
print "Neutre : "
print result[2] * 100, "%"
print "Triste : "
print result[3] * 100, "%"
print "Colere : "
print result[4] * 100, "%"

print ""
print "------------Affichage du sentiment général-----------"
if result[0] == max(result):
    print "==> Enthousiaste"
elif result[1] == max(result):
    print "==> Content"
elif result[2] == max(result):
    print "==> Neutre"
elif result[3] == max(result):
    print "==> Triste"
elif result[4] == max(result):
    print "==> Colere"