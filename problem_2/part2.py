import os
import sys

current_directory = os.getcwd()
input_file = "input.txt"

file = os.path.join(current_directory, input_file)

games = []

with open(file,'r') as f:
    for line in f:
        games.append(line.strip().split(":")[1])

#12 red cubes, 13 green cubes, and 14 blue cubes

# max_cubes = {"red":12,"green":13,"blue":14}
ans = 0
for game in games:
    sets = game.split(";")
    min_cubes = {"red":0,"green":0,"blue":0}
    for set in sets:
        cubes = set.split(",")
        for cube in cubes:
            v,c = cube.split()
            v = int(v)
            min_cubes[c] = max(min_cubes[c],v)
    
    power = 1
    for color in min_cubes:
        power *= min_cubes[color]
    ans += power

    

print(ans)

