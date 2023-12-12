import os

current_directory = os.getcwd()
input_file = "input.txt"

file = os.path.join(current_directory, input_file)

test_cases = []

with open(file,'r') as f:
    for line in f:
        test_cases.append(line.strip())

digits = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
ans = 0

for test_string in test_cases:
    first = ""
    first_word = ""
    string = ""
    found_first = False
    for s in test_string:
        if found_first:
            break
        if s.isdigit():
            if not found_first:
                string += s
                found_first = True
        else:
            if not found_first:
                first_word += s
                for d in digits:
                    if d in first_word:
                        string += str(digits[d])
                        found_first = True
                        break
    
    print(string)

    last_word = ""
    final_word = ""
    found_last = False
    for s in test_string[::-1]:
        if s.isdigit():

            last_word = ""
            if not found_last:
                string += s
                found_last = True
                break

        else:

            last_word = s + last_word
            for d in digits:
                if not found_last and d in last_word:
                    last_word = ""
                    final_word = str(digits[d])
                    string += final_word
                    found_last = True
                    break
            if found_last:
                break

  
    ans+= int(string)
                
print(ans)


