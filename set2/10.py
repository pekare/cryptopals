#!/usr/bin/env python3

import base64
from Crypto.Cipher import AES
from itertools import cycle, islice

file = "10.txt"
test_encrypted = "0gLClNVjy1xEMhvBw3gaEnifC5leA3gsVjKVhLdYZ4X/mLSnrv2xbO4GVZIZfABqULyvKjtFkvkoRUPMM7mTjV4F/IJLWwxcHJ7NIn4nM0d6Rm1qia4/7BVc0xkh6+D6"
key = b"YELLOW SUBMARINE"
iv = b"0000000000000000"

def xor(b_data, b_key):
    cyclic_key = bytes(islice(cycle(b_key),len(b_data)))
    xor_data = bytearray()
    for d, k in zip(b_data, cyclic_key):
        xor_data.append(d ^ k)
    return xor_data

if __name__ == "__main__":
    # with open(file, 'r') as f:
    #     data = base64.b64decode(f.read().rstrip())
    data = base64.b64decode(test_encrypted)
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.encrypt(data)

    print(decrypted_data)