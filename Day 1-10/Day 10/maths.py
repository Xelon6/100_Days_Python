myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people are splitting the bill?: "))
tip = int(input("How many % do you want to tip?: "))
total = myBill + (myBill*(tip/100))
answer = total / numberOfPeople
#um bei einem float nur 2 dezimal stellen zu haben kann ich entweder auf 2 dezimal stellen runden
#answer = round(answer,2)
#oder fix festlegen wie viele dezimal stellen ich haben darf
answer = "{:.2f}".format(answer)
print("You all owe", answer)