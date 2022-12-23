f = open("code/day2/input1.txt", "r")

# Initialize variables
total_score = 0
combo_dict = {"AX": 3, 
"AY": 4, 
"AZ": 8, 
"BX": 1,
"BY": 5, 
"BZ": 9, 
"CX": 2, 
"CY": 6, 
"CZ": 7}

for item in f:
    # Split row 
    item_trim = item.replace('\n', '').replace(' ', '')
    total_score += int(combo_dict[item_trim])

print(total_score)
