import os 
import sys
import math

class Card:
    def __init__(self,card):
        self.card = card
    def __lt__(self,other):
        strength = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,
                    'T':9,'J':0,'Q':11,'K':12,'A':13}
        for i in range(len(self.card)):
            if strength[self.card[i]]==strength[other.card[i]]:
                continue
            elif strength[self.card[i]]<strength[other.card[i]]:
                return True
            else:
                return False


def card_sort(item):
    return item[0]



current_directory = os.getcwd()
input_file = "input.txt"
file = os.path.join(current_directory, input_file)

ans = 0
types = [[] for i in range(7)]

with open(file,'r') as f:
    for line in f:
        card,bid = line.split()
        bid = int(bid)
        hp = {}
        for c in card:
            if c not in hp:
                hp[c] = 1
            else:
                hp[c] +=1

        if len(hp)==1:
            types[6].append([Card(card),bid])
        elif len(hp)==2:
            
            for c in hp:
                if hp[c]==4:
                    if "J" in hp:
                        types[6].append([Card(card),bid])
                    else:
                        types[5].append([Card(card),bid])
                    
                elif hp[c]==3:
                    if "J" in hp:
                        types[6].append([Card(card),bid])
                    else:
                        types[4].append([Card(card),bid])
                    
        elif len(hp)==3:
            cnt = 0

            for c in hp:
                if hp[c]==3:
                    if "J" in hp:
                        types[5].append([Card(card),bid])
                    else:
                        types[3].append([Card(card),bid])
                    break
                elif hp[c]==1 or hp[c]==2:
                    cnt += 1

            if cnt==3:
                if "J" in hp:
                    if hp["J"]==2:
                        types[5].append([Card(card),bid])
                    elif hp["J"]==1:
                        types[4].append([Card(card),bid])
                else:
                    types[2].append([Card(card),bid])
        elif len(hp)==4:
            if "J" in hp:
               types[3].append([Card(card),bid])
            else: 
                types[1].append([Card(card),bid])
        else:
            if "J" in hp:
                types[1].append([Card(card),bid])
            else:
                types[0].append([Card(card),bid])

rank = 1

for i in range(len(types)):
    types[i].sort(key=card_sort)
    for j in range(len(types[i])):
        print(types[i][j][1])
        ans += rank*(int(types[i][j][1]))
        rank += 1

print(ans)


        


                

