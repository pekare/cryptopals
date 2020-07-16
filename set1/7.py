#!/usr/bin/env python3

import base64
from Crypto.Cipher import AES

file = "7.txt"
key = b'YELLOW SUBMARINE'


if __name__ == "__main__":
    with open(file, 'r') as f:
        data = base64.b64decode(f.read().rstrip())
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted_data = cipher.decrypt(data)
    print(decrypted_data.decode('utf-8'))