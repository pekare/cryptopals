#!/bin/env/python3

import base64
import binascii
from string import printable
from itertools import combinations, cycle, islice
from math import sqrt
from collections import Counter

file = "6.txt"

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

def string_candidate(data):
    candidates = []
    for letter in printable:
       # b_data = binascii.unhexlify(data)
        b_key = letter.encode('utf-8')
        xor_data = xor(data, b_key)
        string = xor_data.decode(encoding='utf-8', errors='replace')
        string_score = score(string)
        candidates.append({"data": data, "letter": letter, "string": string, "score": string_score})
    if candidates != []:
        top_candidate = sorted(candidates, key = lambda i: i['score'], reverse=True)[0]
    else:
        top_candidate = None
    return top_candidate

# 2. Write a function to compute the edit distance/Hamming distance between two strings.
#    The Hamming distance is just the number of differing bits.
def hamming_distance(bytes1, bytes2):
    differing_bits = 0
    for b1, b2 in zip(bytes1, bytes2):
        xor_bytes = b1 ^ b2
        differing_bits += bin(xor_bytes).count('1')
    return(differing_bits)

def main():
    with open(file, 'r') as f:
        b64data = f.read().rstrip()
        bytes_data = bytearray(base64.b64decode(b64data))
        # 1. Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
        keysizes = range(2,40)
        # 3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them.
        #    Normalize this result by dividing by KEYSIZE.
        # 4. The KEYSIZE with the smallest normalized edit distance is probably the key.
        #    You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
        normalized_distances = []
        for keysize in keysizes:
            bytes_slice_1 = bytes_data[0:keysize]
            bytes_slice_2 = bytes_data[keysize:2*keysize]
            bytes_slice_3 = bytes_data[2*keysize:3*keysize]
            bytes_slice_4 = bytes_data[3*keysize:4*keysize]
            comb = list(combinations([bytes_slice_1, bytes_slice_2, bytes_slice_3, bytes_slice_4], 2))
            distances = []
            for bytes1, bytes2 in comb:
                distances.append(hamming_distance(bytes1, bytes2) / keysize)
            normalized_distance = sum(distances) / len(distances)
            normalized_distances.append({ "distance": normalized_distance, "keysize": keysize})
        possible = sorted(normalized_distances, key=lambda k: k['distance'])[0]
        print(f"keysize: {possible['keysize']}")
        
        index_dict = {}
        for index in range(0, possible['keysize']):
        	index_dict[index] = []
        	
        for index, byte in enumerate(bytes_data):
        	index_dict[index % possible['keysize']].append(byte)
        
        possible_data = []
        for index in range(0, possible['keysize']):
        	possible_data.append(string_candidate(bytes(index_dict[index]))['letter'])
    
        print("data: " + "".join(possible_data))
        
if __name__ == "__main__":
    main()
