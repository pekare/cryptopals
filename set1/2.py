#!/usr/bin/env python3

import sys
import binascii
import base64

def hex2b64(hexstr):
    data = binascii.unhexlify(hexstr)
    encoded_data = base64.b64encode(data)
    return encoded_data

def xor(data, key):
    xor_data = bytearray()
    for d, k in zip(binascii.unhexlify(data), binascii.unhexlify(key)):
        xor_data.append(d ^ k)
    return binascii.hexlify(xor_data)

def main(argv):
    print(xor(argv[0],argv[1]))

if __name__ == "__main__":
    main(sys.argv[1:])
