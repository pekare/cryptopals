#!/usr/bin/env python3

import sys
import binascii
import base64

def hex2b64(hexstr):
    data = binascii.unhexlify(hexstr)
    encoded_data = base64.b64encode(data)
    return encoded_data

def main(argv):
    print(hex2b64(argv[0]))

if __name__ == "__main__":
    main(sys.argv[1:])
