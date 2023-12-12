import os 
import sys


current_directory = os.getcwd()
input_file = "input.txt"
file = os.path.join(current_directory, input_file)

ans = 0

cnt = 0
seeds = False
seed_to_soil = False
soil_to_fer = False
fer_to_water = False
water_to_light = False
light_to_temp = False
temp_to_hum = False
hum_to_loc = False

all_seeds = []
seed_to_soil_map = {}
soil_to_fer_map = {}
fer_to_water_map = {}
water_to_light_map = {}
light_to_temp_map = {}
temp_to_hum_map = {}
hum_to_loc_map = {}

with open(file,'r') as f:
    for line in f:
        line = line.strip()
        if line:

            if line == "seeds:":
                seeds = True
                seed_to_soil = False
                continue
            elif line == "seed-to-soil map:":
                print("yes")
                seed_to_soil = True
                seeds = False
                continue
            elif line == "soil-to-fertilizer map:":
                soil_to_fer = True
                seed_to_soil = False
                continue
            elif line == "fertilizer-to-water map:":
                print("yes")
                fer_to_water = True
                soil_to_fer = False
                continue
            elif line == "water-to-light map:":
                print("yes")
                water_to_light = True
                fer_to_water = False
                continue
            elif line == "light-to-temperature map:":
                print("yes")
                light_to_temp = True
                water_to_light = False
                continue
            elif line == "temperature-to-humidity map:":
                print("yes")
                temp_to_hum = True
                light_to_temp = False
                continue
            elif line == "humidity-to-location map:":
                print("yes")
                hum_to_loc = True
                temp_to_hum = False
                continue

            if seeds:
                all_seeds = [int(x) for x in line.split()]
            elif seed_to_soil:
                dest,source,r = [int(x) for x in line.split()]
                seed_to_soil_map[source] = [dest,r]
            elif soil_to_fer:
                dest,source,r = [int(x) for x in line.split()]
                soil_to_fer_map[source] = [dest,r]
            elif fer_to_water:
                dest,source,r = [int(x) for x in line.split()]
                fer_to_water_map[source] = [dest,r]
            elif water_to_light:
                dest,source,r = [int(x) for x in line.split()]
                water_to_light_map[source] = [dest,r]
            elif light_to_temp:
                dest,source,r = [int(x) for x in line.split()]
                light_to_temp_map[source] = [dest,r]
            elif temp_to_hum:
                dest,source,r = [int(x) for x in line.split()]
                temp_to_hum_map[source] = [dest,r]
            elif hum_to_loc:
                dest,source,r = [int(x) for x in line.split()]
                hum_to_loc_map[source] = [dest,r]


seed_to_soil_map = dict(sorted(seed_to_soil_map.items()))
soil_to_fer_map = dict(sorted(soil_to_fer_map.items()))
fer_to_water_map = dict(sorted(fer_to_water_map.items()))
water_to_light_map = dict(sorted(water_to_light_map.items()))
light_to_temp_map = dict(sorted(light_to_temp_map.items()))
temp_to_hum_map = dict(sorted(temp_to_hum_map.items()))
hum_to_loc_map = dict(sorted(hum_to_loc_map.items()))

ans = sys.maxsize
for i in range(0,len(all_seeds),2):
    start_seed,ran = all_seeds[i],all_seeds[i+1]
    for seed in range(start_seed,start_seed+ran):
        soil = -1
        fer = -1
        water = -1
        light = -1
        temp = -1
        hum = -1
        loc = -1
        for s in seed_to_soil_map:
            d,r = seed_to_soil_map[s]
            if seed>=s and seed<s+r:
                soil = d+(seed-s)
                break

        if soil == -1:
            soil = seed

        for s in soil_to_fer_map:
            d,r = soil_to_fer_map[s]
            if soil>=s and soil<s+r:
                fer = d+(soil-s)
                break

        if fer == -1:
            fer = soil

        for s in fer_to_water_map:
            d,r = fer_to_water_map[s]
            if fer>=s and fer<s+r:
                water = d+(fer-s)
                break

        if water == -1:
            water = fer

        for s in water_to_light_map:
            d,r = water_to_light_map[s]
            if water>=s and water<s+r:
                light = d+(water-s)
                break

        if light==-1:
            light = water

        for s in light_to_temp_map:
            d,r = light_to_temp_map[s]
            if light>=s and light<s+r:
                temp = d+(light-s)
                break

        if temp == -1:
            temp = light

        for s in temp_to_hum_map:
            d,r = temp_to_hum_map[s]
            if temp>=s and temp<s+r:
                hum = d+(temp-s)
                break

        if hum == -1:
            hum = temp

        for s in hum_to_loc_map:
            d,r = hum_to_loc_map[s]
            if hum>=s and hum<s+r:
                loc = d+(hum-s)
                break

        if loc==-1:
            loc = hum

        ans = min(ans,loc)

print(ans)

        

        
        

        
        




        