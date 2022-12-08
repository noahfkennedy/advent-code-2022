f = open("code/day1/input1.txt", "r")

max_sum = 0
second = 0
third = 0
cur_sum = 0

for item in f:
    if item == '\n':
        if cur_sum > max_sum:
            third = second
            second = max_sum
            max_sum = cur_sum
        elif cur_sum > second:
            third = second
            second = cur_sum
        elif cur_sum > third:
            third = cur_sum
        cur_sum = 0
    else:
        cur_sum += int(item)

print(max_sum + second + third)