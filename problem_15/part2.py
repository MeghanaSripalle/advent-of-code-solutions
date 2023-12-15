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

boxes = [[] for i in range(256)]
for word in input:
    hash_res = 0
    op = ""
    label = ""
    i = 0
    for w in word:
        if w == "=" or w=="-":
            op = w
            i+=1
            break
        label += w
        hash_res += ord(w)
        hash_res *= 17
        hash_res %= 256
        i+=1

    
    if op == "=":
        new_power = int(word[i])
        replaced = False
        i = 0
        for lens in boxes[hash_res]:
            lab,power = lens
            if lab == label:
                replaced = True
                boxes[hash_res][i][1] = new_power
                break
            i+=1
        if not replaced:
            boxes[hash_res].append([label,new_power])
    elif op == "-":
        flag = False
        i = 0
        for lens in boxes[hash_res]:
            lab,power = lens
            if lab == label:
                boxes[hash_res].pop(i)
                break
            i+=1


        
for i in range(len(boxes)):
    if len(boxes[i])>0:
        for j in range(len(boxes[i])):
            lab,po = boxes[i][j]
            ans += (i + 1)*(j+1)*po

print(ans)
