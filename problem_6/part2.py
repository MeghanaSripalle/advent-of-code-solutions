import os 
import sys
import math


current_directory = os.getcwd()
input_file = "input.txt"
file = os.path.join(current_directory, input_file)

ans = 1

cnt = 0
times = []
distances = []
with open(file,'r') as f:
    for line in f:
        if not times:
            times = [int(x) for x in line.split()]
        else:
            distances = [int(x) for x in line.split()]

for i in range(len(times)):
    mindist=sys.maxsize
    maxdist = 0
    for j in range(times[i]+1):
        dist = j*(times[i]-j)
        if dist>distances[i]:
            mindist = j
            maxdist = times[i]-j
            print(dist)
            ans = (abs(maxdist-mindist)+1)
            break


print(ans)

