import random

bingo = [[],[],[]]
def random_number():
    number = random.randint(0,90)
    return number


def prettyPrint():
    for row in bingo:
        print()
        for item in row:
            print(item," ",end='')

numbers = []
for i in range(9):
    numbers.append(random_number())


for i in range(9):
    if i < 3:
        bingo[0].append(numbers[i])
    elif 3 <= i <= 5:
        if i == 4:
            bingo[1].append("BINGO")
        else:
            bingo[1].append(numbers[i])
    elif i > 5:
        bingo[2].append(numbers[i])

prettyPrint()