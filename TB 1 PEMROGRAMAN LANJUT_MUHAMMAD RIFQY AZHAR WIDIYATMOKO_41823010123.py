# Muhammad Rifqy Azhar Widiyatmoko
# 41823010123
# TB 1 - Pemrograman Lanjut

import os
import re

input1 = input().rstrip().split()
A=int(input1[0])
B=int(input1[1])

matrix = []
for _ in range(A):
    list_matrix = input()
    matrix.append(list_matrix)

decode = ""
for y in range(B):
    for z in range(A):
        try:
            decode += matrix[z][y]
        except IndexError:
            pass

pattern = re.findall(r'(?<=[\w])[^\w]+(?=[\w])', decode)
for x in pattern:
    decode = decode.replace(x, ' ', 1)
print(decode)