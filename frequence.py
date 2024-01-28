#!/usr/bin/python3

import sys
from collections import Counter

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Occurences = {}
length = 0

if __name__ == "__main__":
    # Check if a file name is provided as an argument
    if len(sys.argv) == 2:
        # Read from the file
        f = sys.argv[1]
        with open(f, "r") as file:
            s = file.read().strip()
    else:
        # Read from stdin
        s = sys.stdin.read().strip()

    Occurences = Counter(s)
    length = len(s)

    # Print the frequencies
    for c in alphabet:
        print(c, Occurences[c] / length if c in Occurences else 0.0)
