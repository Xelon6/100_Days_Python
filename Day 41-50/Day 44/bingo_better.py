import os
import random
import time

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')
    
bingo = [[],[],[]]
def random_number():
    number = random.randint(0,90)
    return number


def prettyPrint():
    for reihe in bingo:
        for teil in reihe:
            print(teil, end="\t|\t")
        print()


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



while True:
    clear_console()
    print("Your Bingo Card\n")
    prettyPrint()
    x = 0
    try:
        next_number= int(input("\nEnter your Next Number: "))
    except ValueError:
        print("please Enter a valid Number")
        time.sleep(1)
        continue
    
    
    for row in range(3):
        for item in range(3):
            if bingo[row][item] == next_number :
                bingo[row][item] = "X"
                
    for row in bingo:
        for item in row:
            if item =="X":
                x+=1
    if x == 8:
        time.sleep(1)
        clear_console()
        print("You won congrats :)")
        time.sleep(1)
        break