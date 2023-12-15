import os 
import sys
import math
from collections import *

current_directory = os.getcwd()
input_file = "input.txt"
file = os.path.join(current_directory, input_file)

ans = 0
input = []
with open(file,'r') as f:
    for line in f:
        line = line.strip()
        input += line.split(',')

for word in input:
    hash_res = 0
    for w in word:
        hash_res += ord(w)
        hash_res *= 17
        hash_res %= 256

    ans += hash_res

print(ans)
