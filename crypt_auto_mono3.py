#!/usr/bin/python3
import random
import math
import csv
import sys
from collections import Counter

# Function to load tetragram frequencies from a CSV file
def load_tetragram_frequencies(filename):
    frequencies = {}
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                tetragram, frequency = row
                frequencies[tetragram] = int(frequency)
    return frequencies

# Function to evaluate text based on tetragram frequencies
def evaluate_text(text, tetragram_freqs):
    evaluation = 0
    for i in range(len(text)-3):
        tetragram = text[i:i+4]
        if tetragram in tetragram_freqs:
            evaluation += math.log(tetragram_freqs[tetragram])
        else:
            evaluation += math.log(0.001)
    return evaluation

# Function to decrypt text using a given key
def decrypt_text(ciphertext, key):
    key_map = {key[i]: chr(65 + i) for i in range(26)}
    return ''.join(key_map.get(c, c) for c in ciphertext)

# Heuristic functions
def identify_e(ciphertext):
    return Counter(ciphertext).most_common(1)[0][0]

# Placeholder for additional heuristic functions
# ...

# Load the tetragram frequencies
tetragram_freqs = load_tetragram_frequencies('nb_tetra_fr.csv')

# Read ciphertext from file
with open(sys.argv[1], 'r') as file:
    ciphertext = file.read().strip()

# Apply heuristic to identify 'e' as the most frequent letter
mapped_letters = {}
mapped_letters['e'] = identify_e(ciphertext)
# Placeholder for applying other heuristics

# Initial decryption key based on identified letter 'e'
decryption_key = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
most_common_cipher_letter = mapped_letters['e']
decryption_key[decryption_key.index(most_common_cipher_letter)] = 'E'
decryption_key = ''.join(decryption_key)

# Initial setup
ciphertext_eval = evaluate_text(ciphertext, tetragram_freqs)
encryption_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext = ""
plaintext_eval = 0
iter = 0
max_iterations = 10000  # Adjust as necessary
improvement_threshold = 100  # Adjust as necessary
last_improvement = 0

# Main loop
while iter < max_iterations:
    iter += 1
    # ... [same key swapping and improvement logic as before]

# Final output
print("texte chiffré\n" + ciphertext)
print("évaluation " + str(ciphertext_eval))
print("\nAprès " + str(iter) + " itérations, texte déchiffré " + plaintext)
print("substitution appliquée au texte fourni " + encryption_key)
print("clef " + decryption_key)
print("évaluation " + str(plaintext_eval))
