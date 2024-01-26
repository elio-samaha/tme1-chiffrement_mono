#!/usr/bin/python3

# Usage: python3 frequence.py fichier_texte


import sys
from collections import Counter

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Occurences = {}
length = 0

if __name__ == "__main__":
	#if len(sys.argv) != 2:
	#	sys.exit()

	print(f"Arguments count: {len(sys.argv)}")
    
	for i, arg in enumerate(sys.argv):
		print(f"Argument {i:>6}: {arg}" , flush = True)
	
	with open(sys.argv[1] , "r") as file:
		s = file.read().strip()
		Occurences = Counter(s)
		length = len(s)

	# Print the frequences
	for c in alphabet:
		if c in Occurences:
			print (c, Occurences[c] / length)
		else:
			print (c, 0.0)


#"HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"