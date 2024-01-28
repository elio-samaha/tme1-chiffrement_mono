#!/usr/bin/python3

# Usage: python3 cesar.py clef c/d phrase
# Returns the result without additional text

import sys

def chiffrer(c, s):
    return ''.join([chr((((ord(e) - ord("A")) + c) % 26) + ord("A")) if e.isupper() else chr((((ord(e) - ord("a")) + c) % 26) + ord("a")) for e in s])

def dechiffrer(c, s):
    return ''.join([chr((((ord(e) - ord("A")) - c) % 26) + ord("A")) if e.isupper() else chr((((ord(e) - ord("a")) - c) % 26) + ord("a")) for e in s])

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        sys.exit("Usage: python3 cesar.py key c/d phrase")

    e = sys.argv[1]
    clef = (ord(e) - ord("A")) if e.isupper() else (ord(e) - ord("a"))

    c_ou_d, phrase = sys.argv[2], sys.argv[3]
    
    if c_ou_d == "c":
        print(chiffrer(clef, phrase))
    elif c_ou_d == "d":
        print(dechiffrer(clef, phrase))
    else:
        print("Wrong input (Usage: python3 cesar.py key c/d phrase)")
        sys.exit()
