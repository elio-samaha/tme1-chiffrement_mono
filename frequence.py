#!/usr/bin/python3

# Usage: python3 frequence.py fichier_texte


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Occurences = {}
length = 0



# Print the frequences
for c in alphabet:
	if c in Occurences:
		print (c, Occurences[c] / length)
	else:
		print (c, 0.0)


