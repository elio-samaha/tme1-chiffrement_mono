#!/usr/bin/python3

import sys
import random
import operator
from collections import Counter, defaultdict
import json
import csv

#Exo 3)1 :

#⇒ KSWFGAVQXHIBMPUTOYRNJCZELD (Alphabet de Chiffrement Original)
#⇒ FLVZXDEJKUAYMTQNHSBPOGCIRW (Alphabet Réciproque de Déchiffrement)

#Exo 3)2 :

# Usage python3 crypt_auto_mono.py file
# Where file contains the ciphertext
# It is recommended to write a few functions for this exercise


ciphertext = ""
ciphertext_eval = 0
encryption_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext = ""
plaintext_eval = 0
decryption_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
iter = 0

nb_tetra = defaultdict(lambda : 0.001)
with open("nb_tetra_fr.csv" , "r") as file:
    for line in file:
        parts = line.strip().split(';')
        if len(parts) == 2 and parts[0].isalpha() and len(parts[0]) == 4:
            nb_tetra[parts[0]] = int(parts[1])


print((nb_tetra["aebsc"]))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit()
    file_name = sys.argv[1]

    # Do not modify these lines except for variable names
    print ("texte chiffré\n" + ciphertext)
    print ("évaluation " + str(ciphertext_eval))
    print ("\nAprès " + str(iter) + " itérations, texte déchiffré\n" + plaintext)
    print ("substitution appliquée au texte fourni " + encryption_key)
    print ("clef " + decryption_key)
    print ("évaluation " + str(plaintext_eval))



"""

def decrypt(ciphertext, key):
"""
    #Decrypt the ciphertext using the key.
"""
    key_map = {key[i]: ALPHABET[i] for i in range(len(ALPHABET))}
    return ''.join(key_map.get(c, c) for c in ciphertext)

def evaluate(text, tetragram_freqs):
"""
    #Evaluate the quality of the decrypted text using tetragram frequencies.
"""
    score = 0
    for i in range(len(text) - 3):
        tetragram = text[i:i+4]
        if tetragram in tetragram_freqs:
            score += tetragram_freqs[tetragram]
    return score

def load_tetragram_frequencies(filename):
"""
    #Load the tetragram frequencies from the given file.
"""
    frequencies = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2 and parts[0].isalpha() and len(parts[0]) == 4:
                frequencies[parts[0]] = float(parts[1])
    return frequencies

def swap_two_letters(key):
"""
    #Swap two random letters in the decryption key.
"""
    key = list(key)
    a, b = random.sample(range(len(key)), 2)
    key[a], key[b] = key[b], key[a]
    return ''.join(key)

# Main execution starts here
if len(sys.argv) != 2:
    print("Usage: python3 crypt_auto_mono.py <file>")
    sys.exit(1)

# Read the ciphertext from the file
filename = sys.argv[1]
with open(filename, 'r') as file:
    ciphertext = file.read().strip()

# Load tetragram frequencies
tetragram_freqs = load_tetragram_frequencies('nb_tetra_fr.csv')

# Initial decryption key and decrypted text
decryption_key = ALPHABET
plaintext = decrypt(ciphertext, decryption_key)
plaintext_eval = evaluate(plaintext, tetragram_freqs)

# Iterative improvement
max_iterations = 1000
for iter in range(max_iterations):
    new_key = swap_two_letters(decryption_key)
    new_plaintext = decrypt(ciphertext, new_key)
    new_eval = evaluate(new_plaintext, tetragram_freqs)

    if new_eval > plaintext_eval:
        decryption_key = new_key
        plaintext = new_plaintext
        plaintext_eval = new_eval

"""