#!/usr/bin/python3

# Usage: python3 subst_mono.py clef c/d phrase
# Returns the result without additional text

import sys

def chiffrer(c, s):
    return ''.join([c[(ord(e) - ord("A"))]  if e.isupper() else c[(ord(e) - ord("a"))]  for e in s])

def dechiffrer(c, s):
    return ''.join([chr(c.index(e) + ord("A")) if e.isupper() else chr(c.index(e) + ord("a")) for e in s])

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        sys.exit("Usage: python3 subst_mono.py clef c/d phrase")

    clef, c_ou_d, phrase = sys.argv[1], sys.argv[2], sys.argv[3]    

    if c_ou_d == "c":
        print(chiffrer(clef, phrase))
    elif c_ou_d == "d":
        print(dechiffrer(clef, phrase))
    else:
        print("Usage: python3 subst_mono.py clef c/d phrase")
        sys.exit()
    