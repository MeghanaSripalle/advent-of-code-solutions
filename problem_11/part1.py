import os 
import sys
import math
from collections import *


def bfs(i,j,new_grid,done):
    m = len(new_grid)
    n = len(new_grid[0])
    distances = 0
    visited = set()
    queue = deque([[i,j,0]])
    visited.add((i,j))

    while queue:
        x,y,d = queue.popleft()
        if new_grid[x][y] == "#":
            if (x,y) not in done:
                distances += d
        dirs = [[-1,0],[0,-1],[1,0],[0,1]]
        for dx,dy in dirs:
            new_x = x+dx
            new_y = y+dy
            if 0<=new_x<m and 0<=new_y<n and (new_x,new_y) not in visited:
                queue.append([new_x,new_y,d+1])
                visited.add((new_x,new_y))

    return distances

current_directory = os.getcwd()
input_file = "input.txt"
file = os.path.join(current_directory, input_file)

ans = 0
grid = []

with open(file,'r') as f:
    for line in f:
        gal_count = 0
        row = list(line.strip())
        for r in row:
            if r == "#":
                gal_count += 1
            
        if gal_count == 0:
            grid.append(row)
            grid.append(row)
        else:
            grid.append(row)

new_grid = [[] for i in range(len(grid))]
for j in range(len(grid[0])):
    gal_count = 0
    for i in range(len(grid)):
        if grid[i][j] == "#":
            gal_count +=1

    
    for i in range(len(grid)):
        if gal_count == 0:
            new_grid[i].append(grid[i][j])
            new_grid[i].append(grid[i][j])
        else:
            new_grid[i].append(grid[i][j])

ans = 0
done = set()
for i in range(len(new_grid)):
    for j in range(len(new_grid[i])):
        if new_grid[i][j] == "#" and (i,j) not in done:
            ans += bfs(i,j,new_grid,done)
            done.add((i,j))


print(ans)


        

        



