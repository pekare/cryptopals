#!/usr/bin/env python3

import binascii
from collections import Counter

file = "8.txt"

def chunks(list, size):
    for i in range(0, len(list), size):
        yield list[i:i + size]

if __name__ == "__main__":
    possible_ecb = []
    with open(file, 'r') as f:
        line_number = 1
        for line in f:
            data = binascii.unhexlify(line.rstrip())
            split_data = list(chunks(data, 16))
            match = [chunk for chunk, count in Counter(split_data).items() if count > 1]
            if match != []:
                possible_ecb.append({ 'line_number': line_number, 'line': line.rstrip()})
            line_number += 1

    print(possible_ecb)
