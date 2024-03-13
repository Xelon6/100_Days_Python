f = open("D:\\Cybersec\\Python\\100 Days Python\\100_Days_Python\\Day 41-50\\Day 49\\high.score","r",encoding="UTF-8")
scores = f.read().split("\n")
f.close()


max_score = 0
name = ""


for rows in scores:
    data = rows.split()
    if data != []:
        if int(data[1]) > max_score:
            max_score = int(data[1])
            name = data[0]

print(name,max_score)