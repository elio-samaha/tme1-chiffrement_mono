#!/usr/bin/python3

import sys
import random
import operator
from collections import Counter, defaultdict
import json
import csv
import sys
from math import log 
from random import randint

#Exo 3)1 :

#⇒ KSWFGAVQXHIBMPUTOYRNJCZELD (Alphabet de Chiffrement Original)
#⇒ FLVZXDEJKUAYMTQNHSBPOGCIRW (Alphabet Réciproque de Déchiffrement)

#Exo 3)2 :

#!/usr/bin/python3

# Usage python3 crypt_auto_mono.py file
# Where file contains the ciphertext
# It is recommended to write a few functions for this exercise


file = open("nb_tetra_fr.csv")
nb_tetra = dict()
for ligne in file : 
    nb_tetra[ligne[:4]]= int(ligne[5:]) 

ciphertext = open(sys.argv[1]).read()

ciphertext_eval = 0
encryption_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext = ""
plaintext_eval = 0
decryption_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
iter = 0

iter_max = 5000
surplace_max = 1000
surplace = 0

def score(texte):
    e = 0
    for i in range(len(texte) - 3) :
        if texte[i:i+4] in nb_tetra :
            e += log(nb_tetra[texte[i:i+4]])
    return e

def substitution(c1,c2, texte) :
    nvtexte = ""
    for c in texte :
        if c == c1 :
            nvtexte += c2
        elif c==c2 :
            nvtexte +=c1
        else :
            nvtexte +=c
    return nvtexte

plaintext = ciphertext
ciphertext_eval = score(ciphertext)
plaintext_eval = ciphertext_eval
nvscore = 0
nvtexte = ""
while iter < iter_max and surplace <surplace_max :
    i1 = randint(0,25)
    i2 = randint(0,25)
    while(i1==i2) :
        i2 = randint(0,25)
    if i1>i2 : 
        i1,i2 = i2, i1
    #encryption_key[i1] , encryption_key[i2] = encryption_key[i2], encryption_key[i1]
    
    nvtexte = substitution(decryption_key[i1], decryption_key[i2], plaintext )
    nvscore = score(nvtexte)
    if nvscore >= plaintext_eval :
        plaintext_eval = nvscore
        plaintext = nvtexte
        decryption_key = substitution(decryption_key[i1], decryption_key[i2], decryption_key )
    else:
        surplace += 1
    iter += 1

res = ''
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
    res+= chr(decryption_key.index(c) + ord('A'))

encryption_key = res

# Do not modify these lines except for variable names
print ("texte chiffré\n" + ciphertext)
print ("évaluation " + str(ciphertext_eval))
print ("\nAprès " + str(iter) + " itérations, texte déchiffré\n" + plaintext)
print ("substitution appliquée au texte fourni " + encryption_key)
print ("clef " + decryption_key)
print ("évaluation " + str(plaintext_eval))

