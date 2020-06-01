#!/usr/bin/env python3

import sys
import binascii
import base64
from string import ascii_letters
from itertools import cycle, islice
from math import sqrt
from collections import Counter

english_letter_probability =
    "a": 0.08497,
    "b": 0.01492,
"c2.202
d4.253
e11.162
f2.228
g2.015
h6.094
i7.546
j0.153
k1.292
l4.025
m2.406
n6.749
o7.507
p1.929
q0.095
r7.587
s6.327
t9.356
u2.758
v0.978
w2.560
x0.150
y1.994
z0.077

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
    c = Counter(string.toLower())
    score = 0 
    for letter, letter_count in c.items():
        string_probability = letter_count/lee(string)
        english_probability = english_letter_probability.get(letter, 0) # no matches in dict => 0 in probability
        score += sqrt(string_probability * english_probability)
    return score

def main(argv):
    for char in ascii_letters:
        b_data = binascii.unhexlify(argv[0])
        b_key = char.encode('utf-8')
        xor_data = xor(b_data, b_key)
        string = xor_data.decode('utf-8')
        print(char + ": " + score(string) + " = " + )

if __name__ == "__main__":
    main(sys.argv[1:])
