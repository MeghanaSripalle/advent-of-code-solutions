import os 
import sys
import math
from collections import *

current_directory = os.getcwd()
input_file = "input.txt"
file = os.path.join(current_directory, input_file)

ans = 0

def checkAllZeroes(arr):
    if not arr:
        return False
    cnt = 0
    for a in arr:
        if a== 0:
            cnt+=1

    if cnt == len(arr):
        return True
    return False

with open(file,'r') as f:
    for line in f:
        arr = [int(x) for x in line.split()]
        first_values = []
        predicted_val = 0
        while arr and not checkAllZeroes(arr):
            first_values.append(arr[0])
            for i in range(1,len(arr)):
                arr[i-1] = arr[i]-arr[i-1]
            arr.pop()
        
        while len(first_values)>1:
            diff = first_values[-2]-first_values[-1]
            first_values.pop()
            first_values.pop()
            first_values.append(diff)
        

        # print(predicted_val)
        print(first_values)
        ans += first_values[0]
        

print(ans)

