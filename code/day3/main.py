# Initialize
f = open("code/day3/input1.txt", "r")
alph_dct = {}
alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
alphabet = alphabet.replace(' ', '')
sum = 0

# Loop thru and create alphabet dict
for ind, char in enumerate(alphabet):
    alph_dct[char] = ind + 1

def part1():
    for item in f:
        item = item.strip()
        
        ln = len(item)
        print(ln)
        first_half = item[:ln//2]
        second_half = item[ln//2:]

        for char in first_half:
            if char in second_half:
                sum += alph_dct[char]
                break


def part2():
    counter = 0
    sum = 0
    first = ''
    second = ''
    for item in f:
        counter += 1
        item = item.strip()
        if first == '':
            first = item
        elif second == '':
            second = item
        elif counter % 3 == 0:
            print("HEL0")
            for char in item:
                if char in first and char in second:
                    print("Hi")
                    sum += alph_dct[char]
            first = ''
            second = ''
    print(sum)

part2()

