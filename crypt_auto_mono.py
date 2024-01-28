#!/usr/bin/python3

import sys
import random
import operator

# Assume we are working with an uppercase alphabet
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(ciphertext, key):
    """
    Decrypt the ciphertext using the key.
    """
    key_map = {key[i]: ALPHABET[i] for i in range(len(ALPHABET))}
    return ''.join(key_map.get(c, c) for c in ciphertext)

def evaluate(text, tetragram_freqs):
    """
    Evaluate the quality of the decrypted text using tetragram frequencies.
    """
    score = 0
    for i in range(len(text) - 3):
        tetragram = text[i:i+4]
        if tetragram in tetragram_freqs:
            score += tetragram_freqs[tetragram]
    return score

def load_tetragram_frequencies(filename):
    """
    Load the tetragram frequencies from the given file.
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
    Swap two random letters in the decryption key.
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

# Output the results
print("Texte chiffré\n" + ciphertext)
print("Évaluation " + str(evaluate(ciphertext, tetragram_freqs)))
print("\nAprès " + str(max_iterations) + " itérations, texte déchiffré\n" + plaintext)
print("Substitution appliquée au texte fourni " + decryption_key)
print("Clé " + decryption_key)
print("Évaluation " + str(plaintext_eval))
