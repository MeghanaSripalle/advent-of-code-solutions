import os 
import sys


current_directory = os.getcwd()
input_file = "input.txt"
file = os.path.join(current_directory, input_file)

ans = 0

cnt = 0
all_cards = []
with open(file,'r') as f:
    for line in f:
        cnt += 1
        card_set = line.split(":")[1]
        cards = card_set.split("|")
        winning_set = cards[0].split()
        my_set = cards[1].split()

        temp = [winning_set,my_set]
        all_cards.append(temp)


cards_counter = [1 for i in range(cnt)]

i=0
for card_set in all_cards:
        winning_set = set(card_set[0])
        my_set = card_set[1]
        matches = 0
        for card in my_set:
            if card in winning_set:
                matches += 1

        if matches>0:
            for j in range(i+1,min(len(cards_counter),i+matches+1)):
                cards_counter[j] += cards_counter[i]
             
        i+=1
            
        
print(cards_counter)      
print(sum(cards_counter))