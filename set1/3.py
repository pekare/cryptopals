#!/usr/bin/env python3

import sys
import binascii
import base64
from string import ascii_letters
from itertools import cycle, islice

def hex2b64(hexstr):
    data = binascii.unhexlify(hexstr)
    encoded_data = base64.b64encode(data)
    return encoded_data


# bytes in, byted out
def xor(b_data, b_key):
    cyclic_key = bytes(islice(cycle(b_key),len(b_data)))
    xor_data = bytearray()
    for d, k in zip(b_data, cyclic_key):
        xor_data.append(d ^ k)
    return xor_data

def main(argv):
    for char in ascii_letters:
        b_data = binascii.unhexlify(argv[0])
        b_key = char.encode('utf-8')
        xor_data = xor(b_data, b_key)
        print(char + " = " + xor_data.decode('utf-8'))

if __name__ == "__main__":
    main(sys.argv[1:])
