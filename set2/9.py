#!/usr/bin/env python3

input = b"YELLOW SUBMARINE"
block_size = 20

if __name__ == "__main__":
    padding = block_size - (len(input) % block_size)
    padded_input = bytearray(input)
    for i in range(0, padding):
        padded_input.append(padding)
    print(padded_input)
