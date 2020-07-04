#!/usr/bin/env python3

import sys
import binascii
from itertools import cycle, islice

# bytes in, bytes out
def xor(b_data, b_key):
    cyclic_key = bytes(islice(cycle(b_key),len(b_data)))
    xor_data = bytearray()
    for d, k in zip(b_data, cyclic_key):
        xor_data.append(d ^ k)
    return xor_data

def main(argv):
    with open(argv[0], 'r') as f:
        data = f.read().rstrip()
        key = argv[1]
        b_data = data.encode('utf-8')
        b_key = key.encode('utf-8')
        xor_data = xor(b_data, b_key)
        print(
            f"key: {key}\n",
            f"data: {data}\n", 
            f"xor: {xor_data.hex()}"
        )

if __name__ == "__main__":
    main(sys.argv[1:])
