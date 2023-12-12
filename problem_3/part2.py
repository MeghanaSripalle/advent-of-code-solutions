import os
import sys
from collections import *

def isValid(m,n,i,j):
    if i>=0 and i<m and j>=0 and j<n:
        return True
    return False

def checkPartNumber(grid,row,start_index,end_index,gears,num):
    
    flag = False
    
    for j in range(start_index-1,end_index+1):
        if isValid(len(grid),len(grid[0]),row-1,j):
            if not grid[row-1][j].isdigit() and grid[row-1][j] !=".":
                flag =  True
            if grid[row-1][j] =="*":
                key = str(row-1) + "," + str(j)
                gears[key].append(int(num))
                
            
    for j in range(start_index-1,end_index+1):
        if isValid(len(grid),len(grid[0]),row+1,j):
            if not grid[row+1][j].isdigit() and grid[row+1][j] !=".":
                flag =  True
            if grid[row+1][j] =="*":
                key = str(row+1) + "," + str(j)
                gears[key].append(int(num))
            
    if isValid(len(grid),len(grid[0]),row,start_index-1):
            if not grid[row][start_index-1].isdigit() and grid[row][start_index-1] !=".":
                flag =  True
            if grid[row][start_index-1] =="*":
                key = str(row) + "," + str(start_index-1)
                gears[key].append(int(num))
            
    if isValid(len(grid),len(grid[0]),row,end_index):
            if not grid[row][end_index].isdigit() and grid[row][end_index] !=".":
                flag =  True
            if grid[row][end_index] =="*":
                key = str(row) + "," + str(end_index)
                gears[key].append(int(num))
    return flag

current_directory = os.getcwd()
input_file = "input.txt"
file = os.path.join(current_directory, input_file)

grid = []

with open(file,'r') as f:
    for line in f:
        row = list(line.strip())
        grid.append(row)

ans = 0
gears = defaultdict(list)

for i in range(len(grid)):
    num = ""
    found_num = False
    start_index = 0
    end_index = 0
    for j in range(len(grid[i])):
    
        if grid[i][j].isdigit():
            num+=grid[i][j]
            if not found_num:
                start_index = j
                found_num = True
        else:
            if found_num:
                end_index = j
                if checkPartNumber(grid,i,start_index,end_index,gears,num):
                    ans += int(num)
                found_num = False
                start_index = 0
                end_index = 0
                num = ""
        

    if found_num:
        end_index = len(grid[i])
        if checkPartNumber(grid,i,start_index,end_index,gears,num):
            ans += int(num)
        found_num = False
        start_index = 0
        end_index = 0
        num = ""

final = 0
for location in gears:
    if len(gears[location])==2:
        final += gears[location][0]*gears[location][1]
    if len(gears[location])>2:
        print("yes")
    
# print(gears)
print(final)







