# Muhammad Rifqy Azhar Widiyatmoko
# 41823010123
# TB 1 - Pemrograman Lanjut

import re

with open('Kode_NeoMatrix.txt', 'r') as file:
    A, B = map(int, file.readline().rstrip().split())
    MATRIX = [line.rstrip() for line in file]

decoded_looping = " "
for X in range(B):
    for Z in range(len(MATRIX)):
        try:
            decoded_looping += MATRIX[Z][X]
        except IndexError:
            decoded_looping += ' '

decoded = re.sub(r'(?<=[\w])[^\w]+(?=[\w])', ' ', decoded_looping)
print("Decoded :", decoded)