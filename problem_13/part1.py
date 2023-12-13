import os 
import sys
import math
from collections import *
import numpy as np


def checkPalindrome(arr):
    # print(arr)
    n = len(arr)
    for i in range(n//2):
        if arr[i] != arr[n-1-i]:
            return False
    return True

current_directory = os.getcwd()
input_file = "input.txt"
file = os.path.join(current_directory, input_file)

ans = 0
grid = []
k = 0
with open(file,'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            m = len(grid)
            n = len(grid[0])
            check_vertical = False

            last_index = -1
            first_index = -1

            #check first row for vertical lor
            for j in range(1,n,2):
                if checkPalindrome(grid[0][:j+1]):
                    flag = True
                    for i in range(1,m):
                        if not checkPalindrome(grid[i][:j+1]):
                            flag = False
                            break
                    if flag:
                        last_index = j

            if last_index != -1:
                check_vertical = True
                ans += (last_index+1)//2


            if last_index == -1:
                for j in range(n-2,-1,-2):
                    if checkPalindrome(grid[0][j:]):
                        flag = True
                        for i in range(1,m):
                            if not checkPalindrome(grid[i][j:]):
                                flag = False
                                break
                        if flag:
                            first_index = j
                if first_index!=-1:
                    check_vertical = True
                    ans += (n-first_index)//2 + first_index
                
            if not check_vertical:

                new_grid = np.array(grid)
                last_index = -1
                first_index = -1


                #check first column for horizontal lor
                for i in range(1,m,2):
                    if checkPalindrome(new_grid[:i+1,0]):
                        flag = True
                        for j in range(1,n):
                            if not checkPalindrome(new_grid[:i+1,j]):
                                flag = False
                                break
                        if flag:
                            last_index = i
                if last_index != -1:
                    ans += 100*((last_index+1)//2)


                if last_index == -1:
                    for i in range(m-2,-1,-2):
                        if checkPalindrome(new_grid[i:,0]):
                            flag = True
                            for j in range(1,n):
                                if not checkPalindrome(new_grid[i:,j]):
                                    flag = False
                                    break
                            if flag:
                                first_index = i

                    if first_index!=-1:
                        ans += 100*((m-first_index)//2 + first_index)
            print(last_index)
            print(first_index)
            grid = []

        else:
            grid.append(list(line))
            

print(ans)
