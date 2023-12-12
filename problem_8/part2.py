import os 
import sys
import math
from collections import *

current_directory = os.getcwd()
input_file = "input.txt"
file = os.path.join(current_directory, input_file)

ans = 0
num = 0
g = defaultdict(dict)
dirs = ""

cur = deque()
with open(file,'r') as f:
    for line in f:
        line = line.strip()
        if num == 0:
            dirs = line
        elif line:
            start_node,adj = line.split("=")
            start_node = start_node.strip()
            adj = adj.replace("(","").replace(")","")
            left,right = adj.split(",")
            if start_node[-1]=="A":
                cur.append(start_node)
            g[start_node]['L'] = left.strip()
            g[start_node]['R'] = right.strip()

        num+=1

print(cur)

i = 0
j = 0
steps = 0
count = len(cur)

while True:
    
    if j==count:
        print(steps)
        j = 0
        i += 1
        steps+=1
        dest_count = 0
        for c in cur:
            if c[-1]=="Z":
                dest_count+=1
        print("Dest Count: ",dest_count)
        if dest_count==len(cur):
            break
    if i>=len(dirs):
        i = 0
    cur_node = cur.popleft()
    next_node = g[cur_node][dirs[i]]
    cur.append(next_node)
    j+=1
    


print(steps)
    



            
