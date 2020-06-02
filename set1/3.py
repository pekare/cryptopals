#!/usr/bin/env python3

import sys
import binascii
import base64
from string import ascii_letters
from itertools import cycle, islice
from math import sqrt
from collections import Counter

english_letter_probability = {
    "a": 0.08497,
    "b": 0.01492,
    "c": 0.02202,
    "d": 0.04253,
    "e": 0.11162,
    "f": 0.02228,
    "g": 0.02015,
    "h": 0.06094,
    "i": 0.07546,
    "j": 0.00153,
    "k": 0.01292,
    "l": 0.04025,
    "m": 0.02406,
    "n": 0.06749,
    "o": 0.07507,
    "p": 0.01929,
    "q": 0.00095,
    "r": 0.07587,
    "s": 0.06327,
    "t": 0.09356,
    "u": 0.02758,
    "v": 0.00978,
    "w": 0.02560,
    "x": 0.00150,
    "y": 0.01994,
    "z": 0.00077
}

# string in, bytes out
def hex2b64(hexstr):
    data = binascii.unhexlify(hexstr)
    encoded_data = base64.b64encode(data)
    return encoded_data

# bytes in, bytes out
def xor(b_data, b_key):
    cyclic_key = bytes(islice(cycle(b_key),len(b_data)))
    xor_data = bytearray()
    for d, k in zip(b_data, cyclic_key):
        xor_data.append(d ^ k)
    return xor_data

# Bhattacharyya Coefficient
def score(string):
    c = Counter(string.lower())
    score = 0 
    for letter, letter_count in c.items():
        string_probability = letter_count/len(string)
        english_probability = english_letter_probability.get(letter, 0) # no matches in dict => 0 in probability
        score += sqrt(string_probability * english_probability)
    return score

def main(argv):
    for char in ascii_letters:
        b_data = binascii.unhexlify(argv[0])
        b_key = char.encode('utf-8')
        xor_data = xor(b_data, b_key)
        string = xor_data.decode('utf-8')
        print(f"char:{char} score:{score(string)} string:{string}")

if __name__ == "__main__":
    main(sys.argv[1:])
