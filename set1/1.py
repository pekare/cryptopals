#!/usr/bin/env python3

import sys
import binascii
import base64

def main(argv):
    data = binascii.unhexlify(argv[0])
    encoded_data = base64.b64encode(data)
    print(encoded_data)

if __name__ == "__main__":
    main(sys.argv[1:])
