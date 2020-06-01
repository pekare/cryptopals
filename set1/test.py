#!/usr/bin/env python3

from collections import Counter
from math import sqrt

string = "aabbccdd"
string_len = len(string)

c = Counter(string)
english = {
    "a": 0.25,
    "b": 0.25,
    "c": 0.25,
    "d": 0.25
}

for char, count in c.items():
    print(char)
    char_eng_freq = english[char]
    print(char_eng_freq)
    char_str_freq = count/string_len
    print(char_str_freq)
    prob = sqrt(char_eng_freq * char_str_freq)
    print(prob)

