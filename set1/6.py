#!/bin/env/python3

import sys
import base64
from itertools import combinations

file = "/home/carl/projects/cryptopals/set1/6.txt"

# 2. Write a function to compute the edit distance/Hamming distance between two strings.
#    The Hamming distance is just the number of differing bits.
def hamming_distance(bytes1, bytes2):
    differing_bits = 0
    for b1, b2 in zip(bytes1, bytes2):
        xor = b1 ^ b2
        differing_bits += bin(xor).count('1')
    return(differing_bits)

def main():
    with open(file, 'r') as f:
        b64data = f.read().rstrip()
        bytes_data = base64.b64decode(b64data)
        # 1. Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
        keysizes = range(2,40)
        # 3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them.
        #    Normalize this result by dividing by KEYSIZE.
        # 4. The KEYSIZE with the smallest normalized edit distance is probably the key.
        #    You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
        keysizes = []
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
            print(normalized_distance)

if __name__ == "__main__":
    main()
    # bytes_data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20]
    # keysize = 3
    # bytes_slice_1 = bytes_data[0:keysize]
    # bytes_slice_2 = bytes_data[keysize:2*keysize]
    # bytes_slice_3 = bytes_data[2*keysize:3*keysize]
    # comb = list(combinations([bytes_slice_1, bytes_slice_2, bytes_slice_3], 2))
    # for b1, b2 in comb:
    #     print(b1)
    #     print(b2)

