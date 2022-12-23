# Initialize
f = open("code/day4/input1.txt", "r")


low1 = []
high1 = []
low2 = []
high2 = []
counter = 0

for item in f:
    item = item.strip().replace('-', ',').split(',')
    low1.append(int(item[0]))
    high1.append(int(item[1]))
    low2.append(int(item[2]))
    high2.append(int(item[3]))

for i in range(len(low1)):
    if low1[i] <= low2[i] and high1[i] >= high2[i]:
        counter += 1
    elif low2[i] <= low1[i] and high2[i] >= high1[i]:
        counter += 1

2-8
7-61

8-8
7-61

print(counter)