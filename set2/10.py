#!/usr/bin/env python3

import base64
from Crypto.Cipher import AES
from itertools import cycle, islice

file = "10.txt"

def xor(b_data, b_key):
    cyclic_key = bytes(islice(cycle(b_key),len(b_data)))
    xor_array = bytearray()
    for d, k in zip(b_data, cyclic_key):
        xor_array.append(d ^ k)
    return bytes(xor_array)

def chunks(list, size):
    for i in range(0, len(list), size):
        yield list[i:i + size]

def padding(b_data, blocksize):
    padding = blocksize - (len(b_data) % blocksize)
    padded_data = bytearray(b_data)
    for i in range(0, padding):
        padded_data.append(padding)
    return bytes(padded_data)

def cbc_decrypt(b_data, key, iv):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext_blocks = list(chunks(b_data, 16))
    plaintexts = []
    for ciphertext in ciphertext_blocks:
        block = cipher.decrypt(ciphertext)
        plaintext = xor(block, iv)
        iv = ciphertext
        plaintexts.append(plaintext)
    decrypted_data = b''.join(plaintexts)
    return decrypted_data

def cbc_encrypt(b_data, key, iv):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext_blocks = list(chunks(b_data, 16))
    ciphertexts = []
    for plaintext in plaintext_blocks:
        if len(plaintext) < 16:
            block = xor(padding(plaintext, 16), iv)
        else:
            block = xor(plaintext, iv)
        ciphertext = cipher.encrypt(block)
        iv = ciphertext
        ciphertexts.append(ciphertext)
    encrypted_data = b''.join(ciphertexts)
    return encrypted_data

if __name__ == "__main__":
    with open(file, 'r') as f:
        data = base64.b64decode(f.read().rstrip())
        decrypted = cbc_decrypt(data, b'YELLOW SUBMARINE', b'\x00')
        print(decrypted.decode('utf-8'))
        encrypted = cbc_encrypt(decrypted, b'YELLOW SUBMARINE', b'\x00')
        if encrypted == data:
            print("Success")
